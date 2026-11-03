#!/usr/bin/env python3
"""과제 3 재실 인원 정확도 평가 (사진을 저장하지 않는 방식)
  python occ_eval.py sheet --minutes 30                    지금부터 1분 간격 정답지 gt.csv 생성
  (사람이 서비스 값을 보지 말고 각 시각의 실제 인원을 gt.csv 의 count 칸에 적는다)
  python occ_eval.py eval --cam lab1                       logs/service_*.jsonl 과 비교
"""
import argparse, csv, glob, json
from datetime import datetime, timedelta

def sheet(a):
    t = datetime.now().replace(second=0, microsecond=0) + timedelta(minutes=2)
    with open(a.gt, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["time", "count"])
        for i in range(a.minutes):
            w.writerow([(t + timedelta(minutes=i)).strftime("%Y-%m-%dT%H:%M:%S"), ""])
    print(f"{a.gt}: {t:%H:%M}부터 {a.minutes}칸")

def load_preds(pattern, cam):
    out = []
    for p in glob.glob(pattern):
        for line in open(p, encoding="utf-8"):
            r = json.loads(line); c = r.get("cams", {}).get(cam)
            if c and c.get("count") is not None:
                out.append((datetime.fromisoformat(r["ts"]).replace(tzinfo=None), c["count"]))
    return sorted(out)

def evaluate(a):
    preds = load_preds(a.logs, a.cam); assert preds, "서비스 기록이 없음"
    rows = []
    for r in csv.DictReader(open(a.gt)):
        if r["count"].strip() == "":
            continue
        t = datetime.fromisoformat(r["time"])
        pt, pv = min(preds, key=lambda p: abs((p[0] - t).total_seconds()))
        if abs((pt - t).total_seconds()) <= a.tol:
            rows.append((int(r["count"]), pv))
    assert rows, "정답과 맞는 기록이 없음"
    err = [p - g for g, p in rows]
    empty = [(g, p) for g, p in rows if g == 0]
    print(f"정답 {len(rows)}개")
    print(f"MAE {sum(map(abs, err)) / len(err):.2f}명  (기준 1.0 이하)")
    print(f"편향 {sum(err) / len(err):+.2f}명  (음수 = 덜 셈)")
    print(f"정확히 일치 {100 * sum(e == 0 for e in err) / len(err):.0f}%")
    print(f"±1명 이내 {100 * sum(abs(e) <= 1 for e in err) / len(err):.0f}%  (기준 80% 이상)")
    if empty:
        print(f"빈 방 오판율 {100 * sum(p >= 1 for _, p in empty) / len(empty):.0f}%  (기준 10% 이하, {len(empty)}칸)")
    else:
        print("빈 방 정답이 없음: 사람이 없는 시간도 넣어야 빈 방 오판율을 낼 수 있음")
    for n in sorted({g for g, _ in rows}):
        e = [abs(p - g) for g, p in rows if g == n]
        print(f"  실제 {n}명: {len(e)}칸, MAE {sum(e) / len(e):.2f}")

ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="cmd", required=True)
s = sub.add_parser("sheet"); s.add_argument("--minutes", type=int, default=30); s.add_argument("--gt", default="gt.csv"); s.set_defaults(fn=sheet)
e = sub.add_parser("eval"); e.add_argument("--cam", default="lab1"); e.add_argument("--gt", default="gt.csv")
e.add_argument("--logs", default="logs/service_*.jsonl"); e.add_argument("--tol", type=float, default=45); e.set_defaults(fn=evaluate)
a = ap.parse_args(); a.fn(a)

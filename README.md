# embedding_gemma2 — Jetson EmbeddingGemma 2 멀티모달 임베딩 실습 (2팀)

Jetson Orin Nano Super 8GB에서 EmbeddingGemma 2를 설치해 텍스트·영상·음성 임베딩을 돌리고, 도메인 미세조정, 웹캠 물체 검색, 사람 동작·행동 인식, 카메라 2대 접근 감지까지 1~10단계를 수행했다.

| 단계 | 한 일 | 핵심 결과 |
| --- | --- | --- |
| 1~5 환경 | JetPack 7.2.1(CUDA 13.2)용 PyTorch `+cu132`, 가상환경 `~/eg2`, 스왑 8GB, MAXN_SUPER | GPU 행렬 연산 확인 |
| 6 성능 측정 | 텍스트 / +비전 / +오디오 / 전체 구성 | 전체 구성도 8GB에서 동작, 로드 후 RAM 약 5,929MB, 텍스트 질의 158ms |
| 7 도메인 미세조정 | 강의실 문서 20개 × 질문 4개, 약 64초 학습 | accuracy@1 0.85 → 0.90, ndcg@10 0.938 → 0.95 |
| 8 물체 검색 | yolo / relabel / yoloe 비교 | YOLO가 모르는 물체 3개: yolo 0개, relabel 3개 정답 |
| 9 동작·행동 인식 | 규칙(raw / smooth) vs GRU 학습 | smooth로 깜빡임 제거, GRU가 처음 본 사람 15번 중 13번(87%) |
| 10 접근 감지 | 교육장 VIGI + C920 2대: 렌즈·위치 보정, ankle1 / stereo / fused, 타겟 알람 | 렌즈 RMS 0.727 / 0.169px, 칸 크기 24.1 vs 24.0mm, stereo 흔들림 약 3cm, 알람 시나리오 3회 이상 정상 (10-7 거리표·10-8은 가상 시험) |

## 결과 보고서

- **[결과 보고서 (report.md)](report/report.md)** ← 이 파일이 결과 보고서다
- [PDF 버전 (report.pdf)](report/report.pdf)

10단계는 실측이 필요한 항목(보정, 세 방식의 실제 위치, 알람, 앱 자원)은 교육장에서 쟀고, 같은 지점 반복 비교(10-7 거리표)와 이동 타겟(10-8)만 가상 시험(합성 영상)으로 했다. 보고서에 구분해 표시했다.

## 폴더 구성

| 폴더 | 내용 |
| --- | --- |
| `01-06_setup_benchmark/` | 텍스트·비전·오디오·동영상 임베딩 시험(`test_*.py`), 성능 측정(`measure*.py/sh`), 검색 평가(`eval_ir.py`) |
| `07_finetune/` | 미세조정 스크립트(`train_ft*.py`), 학습·평가 데이터(`data/`), 학습 로그, 모델 설정(`model_config/`, 가중치 제외) |
| `08_object_search/` | 웹캠 물체 검색 앱(`app.py`: yolo / relabel / yoloe), 촬영 도구, `camera_tools/` |
| `09_pose_action/` | 동작·행동 인식 앱(`pose_app.py`), GRU 학습(`train_pose.py`), 녹화 특징 CSV(`data/`), 디버그 도구 |
| `10_proximity/team_classroom/` | 교육장 카메라 2대(VIGI + C920) 코드: 카메라 입력(`camsrc.py`), 렌즈 보정(`calib_intrinsics.py`), 체커보드 위치 보정(`calib_board.py`), 접근 감지 앱(`proximity_app.py`), 삼각측량(`stereo.py`), 10-7 가상 거리표(`mode_sim.py`)와 모드별 자원 측정(`mode_bench.sh`), 보정 결과(`calib/`) |
| `10_proximity/virtual_test/` | 10-8 이동 타겟 가상 시험(`vprox.py`, 공통 모듈 `vscene.py`)과 결과 |
| `report/` | 결과 보고서 (report.md, report.pdf), 과제 안내문 |

## 실행

원래는 젯슨의 한 폴더(`~/eg2-lab`)에서 실행했다. 저장소는 단계별로 나눠 정리했으므로, 다시 실행할 때는 파일을 한 폴더에 모은다(예: `train_ft.py`는 `eval_ir.py`를 불러온다).

```bash
cd ~/eg2-lab && source ~/eg2/bin/activate
python 01-06_setup_benchmark/test_all.py
python 07_finetune/train_ft.py
python 08_object_search/app.py --mode relabel
python 09_pose_action/pose_app.py --behavior --model models/action.pt --model models/behavior.pt
python 10_proximity/team_classroom/proximity_app.py --cams vigi 0 --mode fused --port 8011
```

## 보안·개인정보

- 카메라 비밀번호는 환경 변수 `CAM_PW`로만 읽고 코드에 쓰지 않는다.
- Tailscale 주소와 카메라 MAC 주소는 저장소에 넣지 않는다(`<보드 주소>`로 표기, MAC은 환경 변수 `VIGI_MAC`).
- 모델 가중치(`*.pt`, `*.safetensors`), 녹화 영상, 사람이 나오는 이미지(보정용 스냅샷 포함)는 올리지 않았다.

## 환경

Jetson Orin Nano Super 8GB, JetPack 7.2.1(Jetson Linux R39.2.1), Ubuntu 24.04, CUDA 13.2, Python 3.12.3

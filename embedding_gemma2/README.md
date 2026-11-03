# embedding_gemma2 — Jetson EmbeddingGemma 2 멀티모달 임베딩 실습 (2팀)

Jetson Orin Nano Super 8GB에서 EmbeddingGemma 2를 설치해 텍스트·영상·음성 임베딩을 돌리고, 도메인 미세조정, 웹캠 물체 검색, 사람 동작·행동 인식, 카메라 2대 접근 감지까지 1~10단계를 수행했다.

| 단계 | 한 일 | 핵심 결과 |
| --- | --- | --- |
| 1~5 환경 | JetPack 7.2.1(CUDA 13.2)용 PyTorch `+cu132`, 가상환경 `~/eg2`, 스왑 8GB, MAXN_SUPER | GPU 행렬 연산 확인 |
| 6 성능 측정 | 텍스트 / +비전 / +오디오 / 전체 구성 | 전체 구성도 8GB에서 동작, 로드 후 RAM 약 5,929MB, 텍스트 질의 158ms |
| 7 도메인 미세조정 | 강의실 문서 20개 × 질문 4개, 약 64초 학습 | accuracy@1 0.85 → 0.90, ndcg@10 0.938 → 0.95 |
| 8 물체 검색 | yolo / relabel / yoloe 비교 | YOLO가 모르는 물체 3개: yolo 0개, relabel 3개 정답 |
| 9 동작·행동 인식 | 규칙(raw / smooth) vs GRU 학습 | smooth로 깜빡임 제거, GRU가 처음 본 사람 15번 중 13번(87%) |
| 10 접근 감지 | 렌즈·위치 보정, ankle1 / stereo / fused 비교 | 렌즈 RMS 0.13~0.34px, 어깨 삼각측량 평균 오차 0.10m vs 발목 0.66m (가상 시험) |

자세한 표·측정 조건·원인 분석은 `report/report.pdf`를 본다. 10-3~10-8은 가상 시험(합성 영상)으로 진행했고 보고서에 그렇게 표시했다.

## 폴더 구성

| 폴더 | 내용 |
| --- | --- |
| `01-06_setup_benchmark/` | 텍스트·비전·오디오·동영상 임베딩 시험(`test_*.py`), 성능 측정(`measure*.py/sh`), 검색 평가(`eval_ir.py`) |
| `07_finetune/` | 미세조정 스크립트(`train_ft*.py`), 학습·평가 데이터(`data/`), 학습 로그, 모델 설정(`model_config/`, 가중치 제외) |
| `08_object_search/` | 웹캠 물체 검색 앱(`app.py`: yolo / relabel / yoloe), 촬영 도구, `camera_tools/` |
| `09_pose_action/` | 동작·행동 인식 앱(`pose_app.py`), GRU 학습(`train_pose.py`), 녹화 특징 CSV(`data/`), 디버그 도구 |
| `10_proximity/team_classroom/` | 교육장 카메라 2대(VIGI + C920) 코드: 렌즈 보정, 체커보드 위치 보정(`calib_board.py`), 접근 감지 앱(`proximity_app.py`) |
| `10_proximity/home_tablets/` | 집 환경 렌즈 보정(`calib_intr_fast.py`: 최신 프레임만 사용, 3x3 칸 고루 찍기, 오차 큰 사진 자동 제외) |
| `10_proximity/virtual_test/` | 가상 카메라 2대 + 합성 영상 시험(`vstereo.py` 세 방식 비교, `vprox.py` 세 지점·접근 알람·TTC)과 결과 |
| `report/` | 결과 보고서, 과제 안내문 |

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
- 모델 가중치(`*.pt`, `*.safetensors`), 녹화 영상, 사람이 나오는 이미지는 올리지 않았다.

## 환경

Jetson Orin Nano Super 8GB, JetPack 7.2.1(Jetson Linux R39.2.1), Ubuntu 24.04, CUDA 13.2, Python 3.12.3

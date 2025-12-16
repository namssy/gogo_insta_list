# Instagram Follower Tracker

Instagram 프로필 정보를 수집하고, 프로필 사진을 로컬에 다운로드하여 GitHub Pages로 배포하는 도구입니다.

## 기능

- 사용자 목록에서 Instagram 프로필 정보 조회
- 프로필 사진을 로컬 `assets/` 폴더에 다운로드
- 비공개/공개 계정 표시
- 모던하고 반응형인 HTML 페이지 생성
- GitHub Pages 자동 배포

## 설치

```bash
# 저장소 클론
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

# 가상환경 생성 및 활성화
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

## 사용법

### 1. 사용자 목록 작성

`users.txt` 파일에 확인하고 싶은 Instagram 계정을 한 줄에 하나씩 작성합니다.

```
# 주석은 #으로 시작
@username1
@username2
username3
```

> `@`는 있어도 없어도 자동으로 처리됩니다.

### 2. 스크립트 실행

```bash
python main.py
```

실행 결과:
- `index.html` - 생성된 웹 페이지
- `assets/` - 다운로드된 프로필 이미지

### 3. 결과 확인

`index.html` 파일을 브라우저에서 열어 결과를 확인합니다.

## GitHub Pages 배포

### 초기 설정

1. GitHub에 저장소 생성
2. 코드 push:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```
3. **Settings → Pages → Source**에서 **GitHub Actions** 선택

### 업데이트 배포

```bash
# 로컬에서 스크립트 실행
python main.py

# 변경사항 커밋 및 push
git add .
git commit -m "Update follow list"
git push
```

`main` 브랜치에 push하면 GitHub Actions가 자동으로 배포합니다.

## 프로젝트 구조

```
.
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions 배포 워크플로우
├── assets/                 # 다운로드된 프로필 이미지
│   ├── username1.jpg
│   └── default.svg
├── main.py                 # 메인 스크립트
├── users.txt               # 확인할 사용자 목록
├── requirements.txt        # Python 의존성
├── index.html              # 생성된 HTML 파일
└── README.md
```

## 주의사항

- **Rate Limit**: Instagram API 제한으로 인해 요청 간 3초 딜레이가 있습니다.
- **로그인 불필요**: 공개 프로필 정보만 수집하므로 로그인이 필요 없습니다.
- **캐싱**: 이미 다운로드된 이미지는 다시 다운로드하지 않습니다.

## 라이선스

MIT License


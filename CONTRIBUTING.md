# 기여 가이드 (Contributing Guide)

이 프로젝트에 관심을 가져주셔서 감사합니다! 여러분의 기여는 프로젝트를 더 좋게 만드는 데 큰 도움이 됩니다.

## 기여 방법

### 1. 이슈(Issue) 확인 및 생성

작업을 시작하기 전에 [Issues](https://github.com/namssy/gogo_insta_list/issues) 탭을 확인하여 이미 논의 중인 내용이 있는지 확인해 주세요.
- 새로운 기능을 제안하거나 버그를 발견했다면 새로운 이슈를 생성해 주세요.
- 기존 이슈에 기여하고 싶다면 댓글로 작업 의사를 밝혀 주세요.

### 2. 개발 환경 설정

1. 저장소를 포크(Fork)하고 로컬에 클론(Clone)합니다.
   ```bash
   git clone https://github.com/YOUR_USERNAME/gogo_insta_list.git
   cd gogo_insta_list
   ```

2. 가상환경을 생성하고 의존성을 설치합니다.
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

### 3. 개발 진행

- `main.py`를 수정하거나 기능을 추가합니다.
- 코드를 수정한 후에는 반드시 테스트를 진행해 주세요.
  ```bash
  python main.py
  ```
- `index.html`이 정상적으로 생성되는지 확인합니다.

### 4. 커밋 및 푸시 (Commit & Push)

- 커밋 메시지는 명확하게 작성해 주세요. (예: `feat: 사용자 검색 기능 추가`, `fix: 이미지 다운로드 오류 수정`)
- 작업한 내용을 본인의 저장소(Forked Repo)로 푸시합니다.
  ```bash
  git push origin feature/your-feature-name
  ```

### 5. 풀 리퀘스트 (Pull Request) 생성

- 원본 저장소(Original Repo)로 Pull Request를 생성합니다.
- 변경 사항에 대한 명확한 설명을 작성하고, 관련된 이슈가 있다면 링크를 걸어주세요.

## 코드 스타일

- **Python**: PEP 8 스타일 가이드를 준수해 주세요.
- **HTML/CSS**: 가독성을 위해 들여쓰기를 일관되게 유지해 주세요.

감사합니다! 🚀

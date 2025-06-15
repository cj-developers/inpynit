# 🚀 inpynit

**In**finite + **Py**thon + **Init** = 무한한 가능성을 가진 파이썬 프로젝트 시작!

inpynit는 파이썬 프로젝트를 빠르고 쉽게 시작할 수 있도록 도와주는 CLI 도구입니다. 다양한 프로젝트 템플릿과 모던한 설정을 제공합니다.

## ✨ 특징

- 🎯 **다양한 템플릿**: 웹 앱, CLI 도구, 데이터 사이언스, API 등
- 🔧 **모던한 설정**: pyproject.toml, pre-commit, GitHub Actions 등
- 🎨 **사용자 정의**: 프로젝트 요구사항에 맞는 커스터마이징
- 📦 **의존성 관리**: poetry, pip-tools, 또는 requirements.txt 선택
- 🚀 **즉시 실행**: 설치 후 바로 사용 가능한 프로젝트 구조

## 🔧 설치

### pipx 방식 (권장)

**pipx**는 파이썬 CLI 도구를 격리된 환경에서 전역적으로 설치할 수 있게 해주는 도구입니다.
시스템 파이썬 환경을 깨뜨리지 않으면서 CLI 도구를 안전하게 설치하고 관리할 수 있습니다.

#### pipx 설치

```bash
# macOS (Homebrew)
brew install pipx

# Ubuntu/Debian
sudo apt install pipx

# 또는 pip로 설치
pip install --user pipx
pipx ensurepath
```

#### inpynit 설치

```bash
pipx install inpynit
```

### conda 방식

```bash
conda install -c conda-forge inpynit
```

### pip 방식

```bash
pip install inpynit
```

## 🚀 사용법

### 기본 사용법

```bash
# 새 프로젝트 생성
inpynit create my-awesome-project

# 특정 템플릿으로 프로젝트 생성
inpynit create my-web-app --template fastapi

# 인터랙티브 모드
inpynit create my-project --interactive
```

### 사용 가능한 템플릿

- `basic` - 기본 파이썬 패키지
- `fastapi` - FastAPI 웹 애플리케이션
- `flask` - Flask 웹 애플리케이션
- `cli` - Click 기반 CLI 도구
- `datascience` - 데이터 사이언스 프로젝트
- `ml` - 머신러닝 프로젝트

### 예시

```bash
# FastAPI 프로젝트 생성
inpynit create my-api --template fastapi --author "홍길동" --email "hong@example.com"

# 데이터 사이언스 프로젝트 생성
inpynit create data-analysis --template datascience --python-version 3.11
```

## 🛠️ 개발

### conda 방식 (권장)

```bash
# 개발 환경 설정
git clone https://github.com/yourusername/inpynit.git
cd inpynit
conda create -n inpynit-dev python=3.11 -y
conda activate inpynit-dev
pip install -e ".[dev]"

# 테스트 실행
pytest

# 코드 포매팅
black .

# 타입 체크
mypy inpynit
```

### pip 방식

```bash
# 개발 환경 설정
git clone https://github.com/yourusername/inpynit.git
cd inpynit
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는 venv\Scripts\activate  # Windows
pip install -e ".[dev]"
```

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 🤝 기여

기여를 환영합니다! Pull Request를 보내주세요.

---

**inpynit**로 무한한 가능성의 파이썬 프로젝트를 시작해보세요! 🐍✨

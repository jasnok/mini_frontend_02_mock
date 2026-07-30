# 프론트엔드·백엔드 통합 설치 및 실행 가이드

이 문서는 현재 작업공간에 있는 두 프로젝트를 각각 설치하고 함께 실행하는 방법을 설명한다.

- `frontend/`: Streamlit 웹 애플리케이션
- `backend/`: FastAPI API 서버

명령어는 Windows PowerShell을 기준으로 작성되었다.

## 1. 사전 준비

다음 프로그램이 필요하다.

- Python 3.11 이상
- PowerShell
- Gemini 채팅 API를 사용할 경우 Google Gemini API 키

프로젝트 루트에서 Python 버전을 확인한다.

```powershell
cd C:\mini_frontend\mini_frontend_02_mock
python --version
```

## 2. 백엔드 설정

### 2.1 가상환경 생성

프로젝트 루트에서 다음 명령을 실행한다.

```powershell
cd C:\mini_frontend\mini_frontend_02_mock\backend
python -m venv .venv
```

### 2.2 가상환경 활성화

```powershell
.\.venv\Scripts\Activate.ps1
```

PowerShell 실행 정책으로 활성화가 차단되면 현재 터미널에만 적용되는 실행 정책을 설정한 후 다시 활성화한다.

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 2.3 패키지 설치

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 2.4 환경 변수 설정

`backend` 폴더에 `.env` 파일을 만들고 다음 값을 입력한다.

```env
GEMINI_API_KEY=발급받은_API_키
GEMINI_MODEL=gemini-2.5-flash-lite
```

주의 사항:

- `.env` 파일은 Git에 커밋하지 않는다.
- 실제 API 키를 README, 소스 코드 또는 터미널 출력에 남기지 않는다.
- 상품 API만 확인할 때는 Gemini API 키가 없어도 되지만, `/chat/gemini` 호출은 실패한다.

### 2.5 백엔드 실행

백엔드 가상환경이 활성화된 터미널에서 실행한다.

```powershell
cd C:\mini_frontend\mini_frontend_02_mock\backend
python -m uvicorn app.main:app --reload
```

기본 접속 주소:

- API 서버: <http://127.0.0.1:8000>
- Swagger API 문서: <http://127.0.0.1:8000/docs>
- ReDoc API 문서: <http://127.0.0.1:8000/redoc>

현재 백엔드에는 상품 및 Gemini 채팅 API가 구현되어 있다. 프론트엔드 서버 상태 화면이 요청하는 `/health`는 아직 백엔드에 구현되어 있지 않으므로, 해당 화면은 `/health`가 추가되기 전까지 `404 Not Found`를 표시할 수 있다.

### 2.6 백엔드 테스트

서버 실행 터미널과 별개로 실행하거나, 실행 중인 서버를 종료한 뒤 다음 명령을 사용한다.

```powershell
cd C:\mini_frontend\mini_frontend_02_mock\backend
.\.venv\Scripts\Activate.ps1
python -m pytest
```

테스트에서는 Gemini 호출을 모킹하므로 실제 API 요청을 보내지 않는다.

## 3. 프론트엔드 설정

백엔드 실행 터미널은 그대로 두고 새 PowerShell 터미널을 연다.

### 3.1 가상환경 생성

```powershell
cd C:\mini_frontend\mini_frontend_02_mock\frontend
python -m venv .venv
```

### 3.2 가상환경 활성화

```powershell
.\.venv\Scripts\Activate.ps1
```

PowerShell 실행 정책으로 활성화가 차단되면 다음 명령을 사용한다.

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 3.3 패키지 설치

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 3.4 프론트엔드 실행

```powershell
cd C:\mini_frontend\mini_frontend_02_mock\frontend
python -m streamlit run app.py
```

기본 접속 주소:

- Streamlit 화면: <http://localhost:8501>

현재 임시 로그인 계정:

```text
ID: id01
PWD: pwd01
```

이 계정은 실제 백엔드 인증이나 데이터베이스를 사용하지 않고 프론트엔드 코드에서만 확인하는 개발용 계정이다.

## 4. 전체 실행 순서

두 개의 PowerShell 터미널을 사용한다.

### 터미널 1: FastAPI 백엔드

```powershell
cd C:\mini_frontend\mini_frontend_02_mock\backend
.\.venv\Scripts\Activate.ps1
python -m uvicorn app.main:app --reload
```

### 터미널 2: Streamlit 프론트엔드

```powershell
cd C:\mini_frontend\mini_frontend_02_mock\frontend
.\.venv\Scripts\Activate.ps1
python -m streamlit run app.py
```

실행 후 다음 순서로 확인한다.

1. <http://127.0.0.1:8000/docs>에서 백엔드 API 문서가 열리는지 확인한다.
2. <http://localhost:8501>에서 프론트엔드가 열리는지 확인한다.
3. 프론트엔드에서 로그인과 날씨 조회 화면을 확인한다.
4. Swagger 문서에서 상품 API를 호출해 응답을 확인한다.
5. Gemini 환경 변수가 설정된 경우 채팅 API를 호출한다.

## 5. 서버 종료

각 서버가 실행 중인 터미널에서 `Ctrl+C`를 누른다.

가상환경을 종료하려면 다음 명령을 실행한다.

```powershell
deactivate
```

## 6. 문제 해결

### `python` 명령을 찾을 수 없는 경우

Python이 설치되어 있고 PATH 환경 변수에 등록되어 있는지 확인한다. Windows 환경에 따라 `python` 대신 `py` 명령을 사용할 수 있다.

```powershell
py --version
```

### 포트가 이미 사용 중인 경우

백엔드는 다른 포트로 실행할 수 있다.

```powershell
python -m uvicorn app.main:app --reload --port 8001
```

단, 현재 프론트엔드의 백엔드 주소는 `http://127.0.0.1:8000`으로 작성되어 있으므로 포트를 변경하면 프론트엔드 설정도 함께 변경해야 한다.

Streamlit은 다음과 같이 다른 포트를 사용할 수 있다.

```powershell
python -m streamlit run app.py --server.port 8502
```

### 백엔드 모듈을 찾을 수 없는 경우

`backend` 폴더에서 서버를 실행했는지 확인한다.

```powershell
cd C:\mini_frontend\mini_frontend_02_mock\backend
python -m uvicorn app.main:app --reload
```

### Gemini API가 실패하는 경우

- `backend/.env`의 `GEMINI_API_KEY` 값을 확인한다.
- API 키 앞뒤에 불필요한 따옴표나 공백이 없는지 확인한다.
- 설정한 모델을 해당 계정에서 사용할 수 있는지 확인한다.
- API 할당량과 네트워크 연결을 확인한다.
- `.env`를 수정한 뒤 백엔드 서버를 다시 시작한다.

### 프론트엔드에서 백엔드 연결이 실패하는 경우

- 백엔드 터미널에 오류가 없는지 확인한다.
- <http://127.0.0.1:8000/docs>가 열리는지 확인한다.
- 프론트엔드의 `frontend/app_pages/04_health.py`에 설정된 주소와 백엔드 실행 주소가 같은지 확인한다.
- 현재 `/health` API는 구현 전이므로 연결 자체가 성공해도 상태 확인 요청에는 404가 반환될 수 있다.

## 7. 초기화가 필요한 경우

가상환경을 새로 만들려면 해당 서버를 종료한 다음 각 프로젝트의 `.venv` 폴더를 직접 삭제하고, 이 문서의 가상환경 생성 단계부터 다시 진행한다.

사용자 파일이나 소스 코드는 삭제하지 않는다.

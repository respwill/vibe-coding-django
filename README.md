# 메모짱 (vibe-coding-django)

Django 기반의 메모장 웹 애플리케이션

## 주요 기능
- 사용자 회원가입, 로그인, 로그아웃
- 메모 작성, 수정, 삭제, 상세 조회, 목록 조회
- Bootstrap 기반 반응형 UI
- Django Forms 및 crispy-forms 적용

## 설치 및 실행
```bash
python -m venv venv
source venv/bin/activate  # 윈도우: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 폴더 구조
- memojjang/ : Django 프로젝트
- apps/ : Django 앱들 (memos, users)
- templates/ : 템플릿 파일
- static/ : 정적 파일(CSS/JS)
- docs/ : 문서

## 환경 변수 관리
`.env` 파일에서 시크릿, 디버그, 허용 호스트 등 관리

## 테스트
```bash
python manage.py test
```

## 배포
`docs/DEPLOYMENT.md` 참고 (Gunicorn+Nginx 예시 포함)

## 보안
- 입력값 검증, 인증/인가, 시크릿 관리, 불필요한 로그 제거

## 코드 리뷰 및 개선
- PR에 변경 요약/테스트 방법 포함
- 리뷰 개선점 즉시 반영
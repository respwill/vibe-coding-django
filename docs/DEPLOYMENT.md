# 개발 서버 실행
python manage.py runserver

# Gunicorn 실행 예시 (리눅스 환경)
# gunicorn memojjang.wsgi:application --bind 0.0.0.0:8000 --workers 3

# Nginx 설정 예시
# server {
#     listen 80;
#     server_name your_domain.com;
#     location / {
#         proxy_pass http://127.0.0.1:8000;
#         proxy_set_header Host $host;
#         proxy_set_header X-Real-IP $remote_addr;
#         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#         proxy_set_header X-Forwarded-Proto $scheme;
#     }
#     location /static/ {
#         alias /path/to/static/;
#     }
# }

# 환경 변수 및 시크릿 관리 점검
# .env 파일에 시크릿, 디버그, 허용 호스트 등 민감 정보만 저장
# 배포 시 DEBUG=False, 허용 호스트에 실제 도메인 추가

# 베이스 이미지 설정
FROM python:3.9

# 환경 변수 설정
ENV PYTHONUNBUFFERED=1

# 작업 디렉터리 설정
WORKDIR /app

# requirements.txt 파일을 컨테이너의 /app 폴더에 복사
COPY requirements.txt /app/

# 파이썬 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 현재 디렉터리의 모든 파일과 폴더를 컨테이너의 /app 폴더에 복사
COPY . /app/

# 서버 실행 명령어
CMD ["gunicorn", "DG_PRJ.wsgi:application", "--bind", "0.0.0.0:8000"]

RUN pip install gunicorn

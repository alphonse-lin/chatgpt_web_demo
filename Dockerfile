FROM python:3.9
WORKDIR /Documents/002_Xuhui/003_docker/chatgpt_web_demo

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]
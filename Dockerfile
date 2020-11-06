FROM python:3.6-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple

CMD ["python", "app.py"]
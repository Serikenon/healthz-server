FROM python:3.10-slim
WORKDIR /server
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY app.py healthz.py
COPY .env .env
CMD ["python3.10", "healthz.py"]


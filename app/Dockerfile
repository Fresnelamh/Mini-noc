FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir flask prometheus-flask-exporter requests
COPY app.py .
CMD ["python", "app.py"]
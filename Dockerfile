FROM python:3.11-slim

ARG DEFAULT_PORT
ENV DEFAULT_PORT=${DEFAULT_PORT}

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["sh", "-c", "uvicorn app.app:app --host 0.0.0.0 --port ${DEFAULT_PORT}"]

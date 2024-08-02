FROM python:3.11

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ARG DEFAULT_PORT
ENV DEFAULT_PORT=${DEFAULT_PORT}

EXPOSE ${DEFAULT_PORT}

CMD ["sh", "-c", "uvicorn app.app:app --host 0.0.0.0 --port ${DEFAULT_PORT}"]

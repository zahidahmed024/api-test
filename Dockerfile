FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml ./
COPY uv.lock ./
COPY ./app ./app

RUN pip install --upgrade pip && \
  pip install .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

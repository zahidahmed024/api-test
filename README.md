install uv 

uv sync

ENV_FILE=.env.dev uvicorn app.main:app --reload
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim
RUN pip install uvicorn
COPY main.py ./main.py
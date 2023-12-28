FROM python:3.10-slim-buster
RUN pip install uvicorn fastapi
COPY main.py ./main.py

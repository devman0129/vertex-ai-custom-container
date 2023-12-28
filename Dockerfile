FROM python:3.10-slim-buster
WORKDIR .
COPY main.py ./main.py
RUN pip install --upgrade pip
RUN pip install uvicorn fastapi
EXPOSE 8080
ENTRYPOINT [ "python3", "main.py" ]

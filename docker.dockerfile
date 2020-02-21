FROM python:3.8

copy . /app
run pip install -r ./app/requirements.txt
WORKDIR /app
ENTRYPOINT uvicorn main:app --reload --host=0.0.0.0
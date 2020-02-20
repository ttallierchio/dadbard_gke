FROM python:3.8

copy . /app
run pip install -r ./app/requirements.txt
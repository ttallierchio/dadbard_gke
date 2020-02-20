FROM python:3.8

copy ../requirements.txt ./requirements.txt
run pip install -r ./requirements.txt
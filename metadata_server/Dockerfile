FROM python:3.7-slim-buster

WORKDIR /code
ADD . /code

RUN apt-get update
RUN apt-get install nano

RUN python -m pip install -r /code/requirements.txt

COPY . .

CMD ["python", "webapp.py"]



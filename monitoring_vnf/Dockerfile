FROM python:3.7-slim-buster

EXPOSE 5001

WORKDIR /code
ADD . /code

RUN apt-get update
RUN apt-get install nano net-tools

RUN python -m pip install -r /code/requirements.txt

COPY . .

CMD ["python3", "webapp.py"]

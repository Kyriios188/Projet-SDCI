FROM ubuntu:trusty

EXPOSE 5002

WORKDIR /code
ADD . /code


RUN chmod -R 777 /code

RUN apt-get update -y
RUN apt-get install -y \
        nodejs \
        npm \
        nano \
        curl \
        dos2unix

RUN npm config set strict-ssl false

RUN npm cache clean -f
RUN npm install -g n
RUN n 14

RUN npm install url http-forward

ENTRYPOINT node /code/load_balancer.js ; tail -f /dev/null

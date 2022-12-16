FROM ubuntu:trusty

WORKDIR /code
ADD . /code

RUN chmod -R 777 /code

RUN apt-get update -y
RUN apt-get install -y \
	nodejs \
	npm \
	nano \
	wget \
	curl \
	jq \
	dos2unix

RUN npm config set strict-ssl false

RUN npm install express yargs systeminformation request

RUN dos2unix start_server.sh

# set entry point for emulator gatekeeper
ENV VIM_EMU_CMD "echo 'Hello World!'"
ENV VIM_EMU_CMD_STOP "echo 'Stopping the container now.'"

CMD /bin/bash

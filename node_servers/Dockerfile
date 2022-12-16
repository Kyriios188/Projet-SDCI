FROM node:alpine

WORKDIR /code
ADD . /code

RUN chmod -R 777 /code

RUN apk add --update nano wget curl jq
RUN npm install express yargs systeminformation request

RUN dos2unix start_server.sh


# set entry point for emulator gatekeeper
ENV VIM_EMU_CMD "sh start_server.sh"
ENV VIM_EMU_CMD_STOP "echo 'Stopping the container.'"

CMD /bin/sh

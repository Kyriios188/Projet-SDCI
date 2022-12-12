FROM node:alpine

WORKDIR /code
ADD . /code

RUN chmod -R 777 /code

RUN apk add --update nano wget curl jq
RUN npm install express yargs systeminformation request


# set entry point for emulator gatekeeper
ENV VIM_EMU_CMD "echo 'Starting the container.'"
ENV VIM_EMU_CMD_STOP "echo 'Stopping the container.'"

CMD /bin/sh

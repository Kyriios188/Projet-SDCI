FROM node:alpine

WORKDIR /code
ADD . /code

RUN chmod -R 777 /code

# Containernet utils
RUN apk add --update --no-cache \
        bash \
        tcpdump \
        iperf \
        busybox-extras \
        iproute2 \
        iputils

# My utils
RUN apk add nano wget curl jq
#RUN npm install express yargs systeminformation request

RUN dos2unix start_server.sh


# set entry point for emulator gatekeeper
ENV VIM_EMU_CMD "echo 'Hello'"
ENV VIM_EMU_CMD_STOP "echo 'Stopping the container.'"

CMD /bin/sh

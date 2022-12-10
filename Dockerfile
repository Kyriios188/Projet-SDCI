FROM ubuntu:trusty

LABEL maintainer="manuel.peuster@uni-paderborn.de"

WORKDIR /code
ADD . /code

RUN	apt-get update && apt-get install -y \
	net-tools \
    iputils-ping \
	iproute \
    wget
# wget: Besoin pour télécharger les fichiers ? Prof a dit que yen a besoin

# set entry point for emulator gatekeeper
ENV VIM_EMU_CMD "echo 'Hello World!'"
ENV VIM_EMU_CMD_STOP "echo 'Stopping the container now.'"

# CMD should always point to /bin/bash to not block the emulator
CMD /bin/bash
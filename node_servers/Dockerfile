FROM ubuntu:trusty

# You are forced to work with ubuntu:trusty.
# The alpine examples in the containernet github fail
# for any containernet topology here, so node:alpine is doomed.
# You cannot escape this hell. You have to learn what
# is node LTS, how the default node on ubuntu is v <= 1
# and how you can't use the normal manager to update node.

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

# Put this before every npm command
RUN npm config set strict-ssl false


# Update npm otherwise your node doesn't exist an you have to use nodejs v <= 1 
# that can't understand <= or let.
# Can't use nvm because it's not compatible with ubuntu:trusty :D
# This was interesting and important to force students to learn in a project about
# SDN/NFV :DDDDDD

RUN npm cache clean -f
RUN npm install -g n
# Trying each version of node until it worked was very fun.
# Too high and some weird packages go missing. Too low and you can't
# parse the js file.
# If only there was someone that could tell us this!!!
RUN n 14 

RUN npm install express yargs systeminformation request

RUN dos2unix start_server.sh

# set entry point for emulator gatekeeper
ENV VIM_EMU_CMD "sh start_server.sh > logs"
ENV VIM_EMU_CMD_STOP "echo 'Stopping the container now.'"

CMD /bin/bash

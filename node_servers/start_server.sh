echo "Starting container with type: $CONTAINER_TYPE"
SERVER_URL="http://172.18.0.3:5000/"
JS_FILE=""
echo "Server URL: $SERVER_URL"

if [ $CONTAINER_TYPE == "srv" ]; then
    JS_FILE="server.js"
    wget -q https://homepages.laas.fr/smedjiah/tmp/mw/server.js

elif [ $CONTAINER_TYPE == "device1" -o $CONTAINER_TYPE == "device2" -o $CONTAINER_TYPE == "device3" ]; then

    JS_FILE="device.js"
    wget -q https://homepages.laas.fr/smedjiah/tmp/mw/device.js

elif [ $CONTAINER_TYPE == "gwi" -o $CONTAINER_TYPE == "gwf1" -o $CONTAINER_TYPE == "gwf2" -o $CONTAINER_TYPE == "gwf3" ]; then

    JS_FILE="gateway.js"
    wget -q https://homepages.laas.fr/smedjiah/tmp/mw/gateway.js

elif [ $CONTAINER_TYPE == "app" ]; then

    JS_FILE="application.js"
    wget -q https://homepages.laas.fr/smedjiah/tmp/mw/application.js

fi

SERVER_OUTPUT=$(curl -s $SERVER_URL$CONTAINER_TYPE | tr \' \")

LOCAL_IP=$(echo $SERVER_OUTPUT | jq .local_ip)
LOCAL_PORT=$(echo $SERVER_OUTPUT | jq .local_port)
LOCAL_NAME=$(echo $SERVER_OUTPUT | jq .local_name)

echo "Starting $JS_FILE at $LOCAL_IP:$LOCAL_PORT as $LOCAL_NAME"

# We have all the arguments we need
if [ $CONTAINER_TYPE == "srv" ]; then
    node $JS_FILE --local_ip $LOCAL_IP --local_port $LOCAL_PORT --local_name $LOCAL_NAME

# We need remote arguments
else

    REMOTE_IP=$(echo $SERVER_OUTPUT | jq .remote_ip)
    REMOTE_PORT=$(echo $SERVER_OUTPUT | jq .remote_port)
    REMOTE_NAME=$(echo $SERVER_OUTPUT | jq .remote_name)

    echo "Setting parent as $REMOTE_IP:$REMOTE_PORT ($REMOTE_NAME)"

    if [ $CONTAINER_TYPE == "gwi" -o $CONTAINER_TYPE == "gwf1" -o $CONTAINER_TYPE == "gwf2" -o $CONTAINER_TYPE == "gwf3" ]; then

        
        node $JS_FILE --local_ip $LOCAL_IP --local_port $LOCAL_PORT --local_name $LOCAL_NAME --remote_ip $REMOTE_IP --remote_port $REMOTE_PORT --remote_name $REMOTE_NAME


    # We need remote arguments and send_period
    elif [ $CONTAINER_TYPE == "device1" -o $CONTAINER_TYPE == "device2"  -o $CONTAINER_TYPE == "device3" ]; then

        SEND_PERIOD=$(echo $SERVER_OUTPUT | jq .send_period)
        echo "Send period: $SEND_PERIOD"
        node $JS_FILE --send_period $SEND_PERIOD --local_ip $LOCAL_IP --local_port $LOCAL_PORT --local_name $LOCAL_NAME --remote_ip $REMOTE_IP --remote_port $REMOTE_PORT --remote_name $REMOTE_NAME

    fi

fi

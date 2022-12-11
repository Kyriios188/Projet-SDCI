SERVER_OUTPUT=$(curl -s http://172.18.0.2:5000/srv | tr \' \")

LOCAL_IP=$(echo $SERVER_OUTPUT | jq .local_ip)
LOCAL_PORT=$(echo $SERVER_OUTPUT | jq .local_port)
LOCAL_NAME=$(echo $SERVER_OUTPUT | jq .local_name)

echo $LOCAL_IP
echo $LOCAL_PORT
echo $LOCAL_NAME

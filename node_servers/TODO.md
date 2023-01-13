## TODO

-> give up ce qui est demandé par le prof : il ne comprend rien. 
Fait un ENTRYPOINT avec le start-server.sh



## QUESTIONS

-> demander à ajouter les parties stupides et inutiles dans le sujet pour qu'il
n'y ai pas 3 autres années de cette merde.

## COMMANDS

METADATA SERVER (ajouter --network host si dans VM):
docker run -itd --restart unless-stopped --name metasrv kyriios188/metadata-server

NODEJS SERVER (ajouter --network host si dans VM):
docker build -t nodejs .
docker run -itd --name nodejs -e CONTAINER_TYPE="srv" kyriios188/node_server

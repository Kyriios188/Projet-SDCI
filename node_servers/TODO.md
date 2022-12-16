## TODO

-> mininet réussir à déployer les hôtes
==> avec la variable d'environnement

## QUESTIONS


## COMMANDS

METADATA SERVER :
docker run -itd --restart unless-stopped --name metasrv kyriios188/metadata-server

NODEJS SERVER :
docker build -t nodejs .
docker run -itd --name nodejs -e CONTAINER_TYPE="srv" nodejs

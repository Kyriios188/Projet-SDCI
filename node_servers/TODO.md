## TODO

-> Le metadata server n'a pas la bonne adresse IP pour dev3. Dev3 ne met pas à jour
l'adresse ? J'ai cassé quelque chose en détruisant tout ?

-> Dernière séance : j'ai modifié le code du metasrv qui est présent ici
et normalement dans la VM donc c'est pas ça le problème a priori (check ce qui 
en tourne --restart unless-stopped)



## QUESTIONS

-> demander à ajouter les parties stupides et inutiles dans le sujet pour qu'il
n'y ai pas 3 autres années de cette merde.

## COMMANDS

METADATA SERVER (ajouter --network host si dans VM):
docker run -itd --restart unless-stopped --name metasrv kyriios188/metadata-server

NODEJS SERVER (ajouter --network host si dans VM):
docker build -t nodejs .
docker run -itd --name nodejs -e CONTAINER_TYPE="srv" kyriios188/node_server

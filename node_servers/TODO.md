## TODO



## QUESTIONS

-> besoin d'avoir des ports différents ? 8080 8181 8282 9001
-> Qu'est-ce qu'on stocke dans variables d'environnement ? Possible de les stocker dans metasrv à la place ?
Les IP locales je pense que c'est déterminé par la topologie containernet en partie (server, gi, gf123) donc
c'est statique ? Du coup qu'est ce que j'ai à stocker en variables d'environnement ???
-> Pour curl le metadata-server j'ai du faire un network docker et je me connecte au 172.19.0.2.
C'est autorisé pour le metadata-server ? ça va poser problème ? Si faut changer, comment j'autorise le curl
sans network docker ? Avoir tous les containers dans le même network semble contre productif.
-> à quoi sert application.js qui doit être créé en amont ? ?

-> AH le local IP est déterminé par le container qui se lance et se set comme variable d'env ?

## COMMANDS

METADATA SERVER :
docker run -itd -p 5000:5000 --network=net --name metasrv kyriios188/metadata-server

NODEJS SERVER :
docker build -t nodejs .
docker run -itd --network=net --name nodejs -e CONTAINER_TYPE="srv" nodejs

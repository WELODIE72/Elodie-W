## Create a new repository on the command line
echo "# DE-WORKSHOP" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/WELODIE72/ELODIE-W.git
git push -u origin main

## …or push an existing repository from the command line
git remote add origin https://github.com/WELODIE72/ELODIE-W.git
git branch -M main
git push -u origin main


## 1.1 Introduction to Docker

### 1.1.1 Commande pour exécuter un conteneur PostgreSQL 16 avec Docker
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:16

#### Explication des options :
##### -it : 
Exécute le conteneur en mode interactif avec un terminal.
##### -e POSTGRES_USER="root" : 
Définit l'utilisateur PostgreSQL sur "root".
##### -e POSTGRES_PASSWORD="root" : 
Définit le mot de passe pour l'utilisateur PostgreSQL.
##### -e POSTGRES_DB="ny_taxi" : 
Crée une base de données nommée "ny_taxi".
##### -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data : 
Monte le répertoire local ny_taxi_postgres_data pour conserver les données de PostgreSQL.
##### -p 5432:5432 :
Mappe le port 5432 de l'hôte au port 5432 dans le conteneur.
##### postgres:16 : 
Spécifie l'image à utiliser (PostgreSQL version 16).


### ATTENTION  le port 5432 étant utilisé, nous allons chercher à savoir quel processus utilise le port 5432 (ou tout autre port) 

    #### Commandes pour vérifier quel processus occupe un port spécifique comme le 5432:
    ##### a. Avec lsof (List Open Files) :
        sudo lsof -i :5432
    Cette commande liste tous les processus utilisant le port 5432. Elle affichera le PID (Process ID) ainsi que des informations sur le processus

    ##### b. Avec netstat :
        sudo netstat -tuln | grep 5432
    (Cette commande affiche les services en cours d'exécution sur le port 5432. Si PostgreSQL ou un autre service est actif, vous verrez une ligne correspondante.)

    #### Si vous utilisez Docker
    ##### Vous pouvez lister les conteneurs en cours d'exécution et voir les ports qu'ils utilisent comme suit :
        docker ps
    Cela affichera tous les conteneurs en cours d'exécution et les ports qu'ils exposent. Vous pourrez ainsi identifier si l'un de vos conteneurs utilise le port 5432.

    ##### Pour arrêter le processus utilisant le port
        sudo kill <PID>
    Cela vous permettra de libérer le port 5432 si nécessaire.

    #### Résultats :
    (base) ... % sudo lsof -i :5432
    Password:
    COMMAND  PID     USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
    postgres 346 postgres    7u  IPv6 0x9920b939b1bf2e9d      0t0  TCP *:postgresql (LISTEN)
    postgres 346 postgres    8u  IPv4 0x9920b934e67ac145      0t0  TCP *:postgresql (LISTEN)

    #### Explication des options :
    Le résultat de la commande montre que le processus postgres utilise le port 5432 pour écouter à la fois sur les adresses IPv6 et IPv4. Le PID du processus est 346, et il est exécuté par l'utilisateur postgres.

    ##### Pour libérer le port 5432 en arrêtant le service PostgreSQL en cours si non besoin :
    ##### Sous macOS, si PostgreSQL est exécuté via Homebrew, vous pouvez arrêter le service avec :
        brew services stop postgresql
    ##### Tuer le processus : Si PostgreSQL tourne dans un conteneur Docker (ou pour le faire manuellement)
    Utilisez la commande kill pour terminer le processus avec le PID que vous avez obtenu (ici 346) :
        sudo kill 346



##### Pour vérifiez que le conteneur est bien en cours d'exécution avec la commande :
docker ps

    ###### Cela devrait afficher quelque chose comme :
    CONTAINER ID   IMAGE         COMMAND                  CREATED       STATUS       PORTS                    NAMES
<container_id> postgres:16   "docker-entrypoint.s…"   ...           Up X minutes 0.0.0.0:5433->5432/tcp   <container_name>


##### Commande pour se connecter à PostgreSQL depuis votre terminal ou depuis un client PostgreSQL
psql -h localhost -p 5433 -U root -d ny_taxi

##### Explication des options :
-h localhost : se connecte à l'hôte local.
-p 5433 : utilise le port 5433 sur l'hôte (qui est mappé au port 5432 dans le conteneur).
-U root : utilise l'utilisateur root.
-d ny_taxi : se connecte à la base de données ny_taxi.




# Projet avec Flask et MongoDB dans Docker

Ce projet est une application web construite avec Flask, un framework web en Python, qui communique avec une base de données NoSQL MongoDB. Il est conçu pour s'exécuter dans deux conteneurs Docker distincts, un pour le serveur web et un pour la base de données MongoDB, les deux connectés à un réseau local pour permettre la communication entre eux.

## Configuration requise

Avant de démarrer le projet, assurez-vous d'avoir les éléments suivants installés sur votre système :

- Docker (assurez-vous que Docker est correctement configuré et en cours d'exécution)

## Déploiement

```bash
  ./deploy.sh
```

Le script de déploiement effectuera les étapes suivantes :

1. Construira une image Docker pour l'application Flask.
2. Créera un conteneur Docker à partir de l'image de l'application.
3. Construira une image Docker pour la base de données MongoDB.
4. Créera un conteneur Docker pour la base de données MongoDB.
5. Connectera les conteneurs au même réseau local pour permettre la communication.

Après avoir exécuté le script, l'application sera accessible depuis un navigateur Web à l'adresse du server (dans le docker nework) au port 8080.

L'image docker est aussi disponible sur dockerHub : [flask-app](https://hub.docker.com/repository/docker/celiobueri/flask-app)

## Configuration

Si vous avez besoin de personnaliser la configuration de l'application ou de la base de données MongoDB pour l'exécution dans les conteneurs Docker, assurez-vous de vérifier les fichiers de configuration dans le répertoire du projet.

## Fonctionnalités

L'application dispose des fonctionnalités suivantes :

- Affichage des données depuis la base de données MongoDB.
- Ajout de nouvelles données à la base de données. (TODO)
- Modification des données existantes. (TODO)
- Suppression des données de la base de données. (TODO)

## Contribution

Si vous souhaitez contribuer à ce projet, n'hésitez pas à créer une pull request sur GitHub. Votre contribution est la bienvenue.

## Auteurs

- Celio Bueri
- Louis Oger
- Nolan Clerc

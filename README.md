# Projet Django REST API - Reservation

Ce projet est une API Django REST Framework permettant de gérer des artistes (CRUD),
avec authentification, tests automatisés et conteneurisation via Docker.

Le projet peut être lancé et testé facilement sur **Windows, macOS ou Linux**.

---

## Prérequis

- Docker
- Docker Compose

Aucune installation locale de Python, Django ou MySQL n’est nécessaire.

---

## Installation du projet

### 1. Cloner le dépôt

```bash
git clone https://github.com/jpmpindu/pid_api.git
cd reservation
```

---

### 2. Créer le fichier `.env` en modifiant le fichier .env.example

À la racine du projet, créer un fichier `.env` :

```env
MYSQL_DATABASE=non_de_la_base_des_données
MYSQL_USER=nom_user
MYSQL_PASSWORD=mot_de_passe
MYSQL_ROOT_PASSWORD=mot_de_passe_du_root
DATABASE_HOST=db
DATABASE_PORT=3306
```

---

### 3. Lancer le projet avec Docker

```bash
docker-compose up -d --build
```

Services lancés :
- **web** : Django + Django REST Framework
- **db** : MySQL
- **phpmyadmin** : Interface MySQL

Migrations de la base de données

Ce projet utilise les migrations Django pour gérer la création et l’évolution du schéma de la base de données MySQL.

⚠️ Après le premier démarrage des conteneurs, il est obligatoire d’exécuter les migrations afin de créer les tables nécessaires.

Appliquer les migrations

```bash
docker-compose exec web python manage.py migrate
```

Créer de nouvelles migrations

Si vous modifiez ou ajoutez des modèles Django :

docker-compose exec web python manage.py makemigrations

Puis appliquez-les :

```bash
docker-compose exec web python manage.py migrate
```

✔ Les migrations garantissent la cohérence entre le code Python et la structure de la base de données.

---

## Création du superutilisateur

Pour accéder à l’admin Django et tester l’API :

```bash
docker-compose exec web python manage.py createsuperuser
```

Suivre les instructions dans le terminal.

---

## Accès à l’application

### API
- Liste des artistes :  
  http://localhost:8000/api/artists/

⚠️ Authentification requise.

### Admin Django
- http://localhost:8000/admin/


---

## Endpoints CRUD API

| Méthode | URL | Description |
|-------|-----|------------|
| GET | /api/artists/ | Liste des artistes |
| POST | /api/artists/ | Créer un artiste |
| GET | /api/artists/{id}/ | Détails d’un artiste |
| PUT | /api/artists/{id}/ | Modifier un artiste |
| PATCH | /api/artists/{id}/ | Modification partielle |
| DELETE | /api/artists/{id}/ | Supprimer un artiste |

---

## Tests automatisés

Les tests se trouvent dans le dossier :

```
api/tests/
```

Lancer les tests :

```bash
docker-compose exec web python manage.py test api/tests
```

✔ Les tests utilisent une **base de données vierge temporaire**  
✔ Aucune donnée réelle n’est modifiée

---

## Arrêt du projet

```bash
docker-compose down
```

Pour supprimer également les données MySQL :

```bash
docker-compose down -v
```

---

## Technologies utilisées

- Python 3
- Django
- Django REST Framework
- MySQL
- Docker & Docker Compose

---

## Auteur

Projet réalisé par **Jean‑Paul Mpindu Mukandila**  
Dans le cadre d’un projet académique (API REST Django).


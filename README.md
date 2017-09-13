# Inimex API

<p align="center">
  <img src="https://raw.github.com/marcosvbras/inimex-api/master/readme_images/colorful_inimex_logo.png" alt="Custom image"/>
</p>

**Inimex API** is a simple RESTful API that provides anime informations and allow that users to make your own anime lists (like the [MyAnimeList](https://myanimelist.net/)). The anime data is consumed from [Kitsu API](https://kitsu.io/).

Using this API you can:
1. Perform basic CRUD related to animes.
2. Add animes to your lists.

The Inimex API is used for learn more about the magic-huge web world and improve my Jedi Master Programming Skills in Python. This API will be the **Best API** related to animes in the world, **do you doubt it?** 

<p align="center">
  <img src="https://raw.github.com/marcosvbras/inimex-api/master/readme_images/pikachu.jpg" alt="Custom image"/>
</p>

## Requirements
- Python 3.5;
- RabbitMQ 3.6.11.

## Installation
Install all libraries in the `requirements.pip` file:

```
pip install -r requirements.pip
```

> **RECOMMENDED:** Use [Docker](https://www.docker.com/) or a virtual environment (e.g., [VirtualEnv](https://virtualenv.pypa.io/)) to ensure your dependencies are local to your app.

Ensure to make and run the database migrations:

```
python manage.py makemigrations
python manage.py migrate
```

Change the `BROKER_URL` property in `project/settings.py` file based in your RabbitMQ configurations. Ensure that RabbitMQ is running.

## Running the project
Run the application using the Django built in server:

```
python manage.py runserver 0.0.0.0:8000
```

Run Django Celery:

```
celery --app=project worker --loglevel=INFO
```

(Optional) Run Django Celery Flower to tasks monitoring:

```
celery --app=project flower
```

## Stack
- Backend: Python/Django REST Framework
- Broker: RabbitMQ
- Database: SQLite

# License
Copyright 2017 Marcos Vinícius Brás

Licensed under the Do What The F*ck You Want To Public License, version 2.0. 
See the LICENSE file to more informations about this awesome license.

    http://www.wtfpl.net/about/

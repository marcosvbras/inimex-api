Inimex API
=======================

A simple Django REST API that provide anime informations.
The anime data is crawled from [Kitsu API](https://kitsu.io/).

Requirements
-------------------------
- Python 3.5
- RabbitMQ
- (Optional) VirtualEnv

Before to run the project
-------------------------

- Install all libraries from requirements.pip file;
- Change settings.BROKER_URL based in your RabbitMQ configurations;
- Make the database migrations.

After to run the project
-------------------------

- Run Django Celery.
- (Optional) Run Django Celery Flower to tasks monitoring.
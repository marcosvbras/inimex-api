Inimex API
=======================

A simple Django REST API that provide anime informations.
The anime data is consumed from [Kitsu API](https://kitsu.io/).

Requirements
-------------------------
- Python 3.5;
- RabbitMQ;

Before to run the project
-------------------------

- Install on your virtual enviroment or on your host all libraries from requirements.pip file;
- Change settings.BROKER_URL based in your RabbitMQ configurations;
- Make the database migrations.

After to run the project
-------------------------

- Run Django Celery (commands inside celery.sh file);
- (Optional) Run Django Celery Flower to tasks monitoring.

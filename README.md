# Cookiecutter Django Rest
Do you need a ready to production Django rest framework template?. It's our first objective with this
repository.

This repository use [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/index.html) for provide you a quick start
with Django rest framework.

## Features
* Python 3.8+
* Django 3.0+
* PotsgreSQL 13.1+
* Local development fully dockerized via docker-compose.
* Django rest framework.
* Optimized local, test and production settings.
* Multi-task, async tasks and task monitoring.
    * [Celery 4.4.6](https://docs.celeryproject.org/en/stable/)
    * [Redis 6.0.9](https://redis.io/) 
    * [Flower 1.0.0](https://flower.readthedocs.io/en/latest/index.html#)
* Testing with unittest or pytest.
* Dependencies work with [pipenv](https://pipenv.pypa.io/en/latest/).

And more incoming...

## How start
You need to install [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html), one way to do that is:
```
pip install cookiecutter
```
See more ways to install in [cookiecutter installation](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html).

Then, scaffold your project:
```
cookiecutter gh:yulio94/cookiecutter-django-rest 
```
An example in [cride repository](https://github.com/yulio94/cride).

### Thanks to:
* @pablotrinidad
* @pydanny
* @agconti
* @platzi


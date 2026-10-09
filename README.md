# Cookiecutter Django Rest
A Django REST framework template that is ready for production.

It uses [cookiecutter](https://cookiecutter.readthedocs.io/) to give you a quick start with Django REST framework.

## Features
* Python 3.14, Django 5.2 LTS, Django REST framework.
* PostgreSQL 17.
* Dependencies managed with [uv](https://docs.astral.sh/uv/), locked in `uv.lock`.
* Local development fully dockerized with Docker Compose.
* Separate local, test and production settings.
* Async and scheduled tasks with [Celery](https://docs.celeryq.dev/) and [Redis](https://redis.io/) 8.
* OpenAPI schema and Swagger UI at `/api/docs/` via drf-spectacular.
* Production behind [Caddy](https://caddyserver.com/) 2 with automatic HTTPS, Gunicorn, WhiteNoise for static files, S3 for media and Mailgun for email.
* pytest, ruff, mypy and pre-commit.

## How to start
With uv installed, scaffold your project:
```
uvx cookiecutter gh:yulio94/cookiecutter-django-rest
```

Then, inside the new project:
```
cp .envs/.local/django.env.example .envs/.local/django.env
cp .envs/.local/postgresql.env.example .envs/.local/postgresql.env
docker compose -f docker-compose.local.yml up --build
```
The API docs are at http://localhost:8000/api/docs/.

For production, fill in the files under `.envs/.production/` from their `.example` files and run `docker compose -f docker-compose.prod.yml up --build -d`.

An example in [cride repository](https://github.com/yulio94/cride).

### Thanks to:
* @pablotrinidad
* @pydanny
* @agconti
* @platzi

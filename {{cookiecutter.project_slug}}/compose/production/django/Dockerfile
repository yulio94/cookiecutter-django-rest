FROM python:3.14-slim

COPY --from=ghcr.io/astral-sh/uv:0.13.0 /uv /bin/

ENV PYTHONUNBUFFERED=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/venv \
    PATH="/venv/bin:$PATH"

RUN apt-get update \
  && apt-get install -y --no-install-recommends gettext \
  && rm -rf /var/lib/apt/lists/* \
  && useradd --system django

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev

COPY --chmod=755 ./compose/production/django/start /start
COPY --chmod=755 ./compose/production/django/celery/worker/start /start-celeryworker
COPY --chmod=755 ./compose/production/django/celery/beat/start /start-celerybeat

COPY --chown=django . /app

USER django

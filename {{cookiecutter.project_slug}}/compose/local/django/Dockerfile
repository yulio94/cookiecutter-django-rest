FROM python:3.14-slim

COPY --from=ghcr.io/astral-sh/uv:0.13.0 /uv /bin/

ENV PYTHONUNBUFFERED=1 \
    UV_LINK_MODE=copy \
    # Outside /app so the source bind mount does not hide it.
    UV_PROJECT_ENVIRONMENT=/venv \
    PATH="/venv/bin:$PATH"

# gettext for translations, postgresql-client for `manage.py dbshell`
RUN apt-get update \
  && apt-get install -y --no-install-recommends gettext postgresql-client \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --locked

COPY --chmod=755 ./compose/local/django/start /start
COPY --chmod=755 ./compose/local/django/celery/worker/start /start-celeryworker
COPY --chmod=755 ./compose/local/django/celery/beat/start /start-celerybeat

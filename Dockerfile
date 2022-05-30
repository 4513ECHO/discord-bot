FROM python:3.9-buster

ENV POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update \
 && apt-get install --no-install-recommends -y libffi-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip poetry
COPY poetry.lock pyproject.toml /app/
WORKDIR /app
RUN poetry install -vvv --no-dev --no-interaction

COPY ./bot /app/bot

CMD ["python", "-m", "bot"]
# CMD ["bash"]

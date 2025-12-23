RUN python3 -m venv /venv
ENV PYTHON=/venv/bin/python3
RUN $PYTHON -m pip install wheel poetry gunicorn

COPY coe/cmd /app/coe/cmd
COPY poetry.lock pyproject.toml /app/

RUN . /venv/bin/activate \
	&& poetry config virtualenvs.create false \
	&& poetry install --no-interaction --only main

COPY coe/web/static/package.json coe/web/static/package-lock.json coe/web/static/
RUN npm install --prefix coe/web/static

COPY . /app
ENV COE_SETTINGS=.env
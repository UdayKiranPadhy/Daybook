FROM python:3.10-slim

WORKDIR /code

COPY ./daybook-be/. /code

RUN pip install --upgrade pip wheel setuptools pip-tools \
    && python -m pip install -r requirements-dev.txt

EXPOSE 3000


CMD ["uvicorn", "--reload", "--host", "0.0.0.0", "--port", "80", "src.api.app:app"]
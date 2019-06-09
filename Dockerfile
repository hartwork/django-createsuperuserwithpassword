# Copyright (C) 2019 Sebastian Pipping <sebastian@pipping.org>
# Licensed under the MIT license

FROM python:3.7

ENV PATH=${PATH}:/root/.local/bin

RUN apt-get update && apt-get install --yes --no-install-recommends \
        wait-for-it

RUN pip3 install --user \
        psycopg2-binary

COPY docker-entrypoint.sh setup.py        /app/
COPY django_createsuperuserwithpassword/  /app/django_createsuperuserwithpassword/


WORKDIR /app

RUN python3 setup.py develop --user


WORKDIR /

RUN django-admin startproject mysite


WORKDIR /mysite/

RUN echo 'DATABASES = {"default": {"ENGINE": "django.db.backends.postgresql", "NAME": "postgres", "USER": "postgres", "HOST": "postgres", "PORT": 5432}}' >> mysite/settings.py
RUN echo 'ALLOWED_HOSTS = ["*"]' >> mysite/settings.py
RUN echo 'INSTALLED_APPS += ("django_createsuperuserwithpassword", )' >> mysite/settings.py

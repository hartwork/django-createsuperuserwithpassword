#! /usr/bin/env bash
# Copyright (C) 2019 Sebastian Pipping <sebastian@pipping.org>
# Licensed under the MIT license

set -e

PS4='# '
set -x

wait-for-it postgres:5432

python3 manage.py migrate

python3 manage.py createsuperuserwithpassword \
        --username admin \
        --password admin \
        --email admin@example.org \
        --preserve

exec "$@"

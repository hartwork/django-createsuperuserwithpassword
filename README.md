# django-createsuperuserwithpassword

… provides a Django management command
to create ready-to-login super users during development.


# How to Use

## 1. Install

Install the pip package locally or globally:

```shell
pip install [--user] django-createsuperuserwithpassword
```


## 2. Activate

Enable the Django management command by extending your Django project settings:

```python
INSTALLED_APPS += ("django_createsuperuserwithpassword", )
```


## 3. Apply

Call the command — e.g. from within a container entrypoint script — like this:

```shell
python manage.py createsuperuserwithpassword \
        --username admin \
        --password admin \
        --email admin@example.org \
        --preserve
```


# Authors

**django-createsuperuserwithpassword** is based on code
by [Adam Charnock](https://github.com/adamcharnock)
licensed under [the MIT license](https://opensource.org/licenses/MIT)
that started out at [adamcharnock/swiftwind-heroku](https://github.com/adamcharnock/swiftwind-heroku/commits/master/swiftwind_heroku/management/commands/create_superuser_with_password.py).

[Sebastian Pipping](https://github.com/hartwork) added and fixed a few things, on top.


# Development

If you want to help fix a bug, an easy way to spin up a development environment is:

```shell
git clone https://github.com/hartwork/django-createsuperuserwithpassword
cd django-createsuperuserwithpassword
docker-compose up --build
```

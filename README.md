# django-createsuperuserwithpassword

… provides a Django management command
to create ready-to-login super users during development.

To use, first
enable the management command by extending your Django app settings …

```python
INSTALLED_APPS += ("django_createsuperuserwithpassword", )
```

… and then call the command — e.g. from within a container entrypoint script — like this:

```shell
python3 manage.py createsuperuserwithpassword \
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

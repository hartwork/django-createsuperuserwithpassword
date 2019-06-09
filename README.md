# Hi!

**django-createsuperuserwithpassword** provides a Django management command
to create ready-to-login super users during developement.

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

**django-createsuperuserwithpassword** is based on code by [Adam Charnock](https://github.com/adamcharnock) that started out at [adamcharnock/swiftwind-heroku](https://github.com/adamcharnock/swiftwind-heroku/commits/master/swiftwind_heroku/management/commands/create_superuser_with_password.py).
It is licensed under [the MIT license](https://opensource.org/licenses/MIT).

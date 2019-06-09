# Copyright (C) 2017 Adam Charnock <adam@adamcharnock.com>
# Copyright (C) 2019 Sebastian Pipping <sebastian@pipping.org>
# Licensed under the MIT license

from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError


class Command(createsuperuser.Command):
    help = 'Create a superuser and apply a password as well.'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            '--password', dest='password', default=None, required=True,
            help='Specifies the password for the superuser.',
        )
        parser.add_argument(
            '--preserve', dest='preserve', default=False, action='store_true',
            help='Exit normally if the user already exists.',
        )

    def _get_db_manager(self, database):
        return self.UserModel._default_manager.db_manager(database)

    def handle(self, *args, **options):
        password = options.get('password')
        username = options.get(self.UserModel.USERNAME_FIELD)
        database = options.get('database')

        if password and not username:
            raise CommandError('--{} is required if specifying --password.'
                               .format(self.UserModel.USERNAME_FIELD))

        username_filter = {self.UserModel.USERNAME_FIELD: username}

        if username and options.get('preserve'):
            exists = (self._get_db_manager(database)
                      .filter(**username_filter)
                      .exists())
            if exists:
                self.stdout.write(
                    'User exists, exiting normally due to --preserve.')
                return

        options['interactive'] = False  # To not ask for a password

        super(Command, self).handle(*args, **options)

        user = self._get_db_manager(database).get(**username_filter)
        user.set_password(password)
        user.save()

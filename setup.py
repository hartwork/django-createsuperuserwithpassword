#! /usr/bin/env python
# Copyright (C) 2019 Sebastian Pipping <sebastian@pipping.org>
# Licensed under the MIT license

from textwrap import dedent

from setuptools import find_packages, setup

_classifiers = dedent("""\
    Development Status :: 3 - Alpha

    Framework :: Django
    Framework :: Django :: 1.11
    Framework :: Django :: 2.0
    Framework :: Django :: 2.1
    Framework :: Django :: 2.2

    Intended Audience :: Developers

    License :: OSI Approved :: MIT License

    Natural Language :: English

    Programming Language :: Python
    Programming Language :: Python :: 2.7
    Programming Language :: Python :: 3.5
    Programming Language :: Python :: 3.6
    Programming Language :: Python :: 3.7
    Programming Language :: Python :: 3.8
""")

_description = (
    'Django management command'
    ' to create usable super users'
    ', programmatically'
)

_project_url = 'https://github.com/hartwork/django-createsuperuserwithpassword'


if __name__ == '__main__':
    setup(
            name='django-createsuperuserwithpassword',
            url=_project_url,
            description=_description,
            long_description=_description,
            license='MIT',
            version='1.0.1',
            author='Adam Charnock, Sebastian Pipping',
            author_email='sebastian@pipping.org',
            packages=find_packages(),
            classifiers=[c for c in _classifiers.split('\n') if c],
            install_requires=[
                'Django>=1.11',
            ],
            )

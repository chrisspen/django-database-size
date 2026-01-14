django-database-size
=====================

[![](https://img.shields.io/pypi/v/django-database-size.svg)](https://pypi.python.org/pypi/django-database-size) [![Tests](https://github.com/chrisspen/django-database-size/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/chrisspen/django-database-size/actions/workflows/tests.yml) [![](https://pyup.io/repos/github/chrisspen/django-database-size/shield.svg)](https://pyup.io/repos/github/chrisspen/django-database-size)

Adds a page to Django admin that lists the size of all tables in the database.

Installation
------------

    python setup.py install
    
Or via pip with:
    
    pip install django-database-size

Install the appropriate view in /sql (currently only PostgreSQL and MySQL supported).

Add to your INSTALLED_APPS.

Usage
-----

Browse to /admin/database_size/.

Development
-----------

To run unittests across multiple Python versions, install:

    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt-get update
    sudo apt-get install python-dev python3-dev python3.3-minimal python3.3-dev python3.4-minimal python3.4-dev python3.5-minimal python3.5-dev python3.6 python3.6-dev

To run all [tests](http://tox.readthedocs.org/en/latest/):

    export TESTNAME=; tox

To run tests for a specific environment (e.g. Python 2.7 with Django 1.4):
    
    export TESTNAME=; tox -e py39-django2

To run a specific test:
    
    export TESTNAME=.test_example; tox -e py27-django15

To run the [documentation server](http://www.mkdocs.org/#getting-started) locally:

    mkdocs serve -a :9999

To [deploy documentation](http://www.mkdocs.org/user-guide/deploying-your-docs/), run:

    mkdocs gh-deploy --clean

To build and deploy a versioned package to PyPI, verify [all unittests are passing](https://travis-ci.org/chrisspen/django-chroniker), and then run:

    python setup.py sdist
    python setup.py sdist upload


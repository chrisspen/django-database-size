django-database-size
=====================

[![](https://img.shields.io/pypi/v/django-database-size.svg)](https://pypi.python.org/pypi/django-database-size) [![Build Status](https://img.shields.io/travis/chrisspen/django-database-size.svg?branch=master)](https://travis-ci.org/chrisspen/django-database-size) [![](https://pyup.io/repos/github/chrisspen/django-database-size/shield.svg)](https://pyup.io/repos/github/chrisspen/django-database-size)

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

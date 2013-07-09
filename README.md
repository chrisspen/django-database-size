django-database-size
=====================

Adds a page to Django admin that lists the size of all tables in the database.

Installation
------------

    sudo python setup.py install
    
Or via pip with:
    
    sudo pip install django-database-size

Install the appropriate view in /sql (currently only PostgreSQL supported).

Add to your INSTALLED_APPS.

Usage
-----

Browse to /admin/database_size/.
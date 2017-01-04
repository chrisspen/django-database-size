import os
import sys

import django

PROJECT_DIR = os.path.dirname(__file__)

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

ROOT_URLCONF = 'database_size.tests.urls'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'database_size',
    'database_size.tests',
]

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

# Disable migrations.
# http://stackoverflow.com/a/28560805/247542
class DisableMigrations(object):

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return "notmigrations"
#SOUTH_TESTS_MIGRATE = False # Use syncdb <= Django 1.8
SOUTH_TESTS_MIGRATE = True # Use migrate
#if django.VERSION > (1, 8, 0): # > Django 1.8
# if django.VERSION > (1, 7, 0): # > Django 1.8 
#     MIGRATION_MODULES = DisableMigrations()

if django.VERSION < (1, 7, 0):
    SOUTH_MIGRATION_MODULES = {
        'database_size': 'database_size.south_migrations',
    }

USE_TZ = True

AUTH_USER_MODEL = 'auth.User'

SECRET_KEY = 'abc123'

SITE_ID = 1

BASE_SECURE_URL = 'https://localhost'

BASE_URL = 'http://localhost'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.middleware.transaction.TransactionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',    
)

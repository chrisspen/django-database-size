#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from distutils.core import setup, Command
import database_size

setup(
    name='django-database-size',
    version=database_size.__version__,
    description='Monitor the size of database tables from Django admin.',
    author='Chris Spencer',
    author_email='chrisspen@gmail.com',
    url='http://github.com/chrisspen/django-database-size',
    packages=[
        'database_size',
    ],
    package_data = {
        'database_size': [
            'sql/*.*',
        ],
    },
    #https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: PL/SQL',
    ],
    install_requires = ['Django>=1.4'],
)
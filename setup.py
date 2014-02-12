#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from distutils.core import setup, Command
import database_size

def get_reqs(reqs=[]):
    # optparse is included with Python <= 2.7, but has been deprecated in favor
    # of argparse.  We try to import argparse and if we can't, then we'll add
    # it to the requirements
    try:
        import argparse
    except ImportError:
        reqs.append("argparse>=1.1")
    return reqs

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
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    requires = ["Django>=1.4",],
)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages, Command

import database_size

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

def get_reqs(*fns):
    lst = []
    for fn in fns:
        for package in open(os.path.join(CURRENT_DIR, fn)).readlines():
            package = package.strip()
            if not package:
                continue
            lst.append(package.strip())
    return lst

setup(
    name='django-database-size',
    version=database_size.__version__,
    description='Monitor the size of database tables from Django admin.',
    author='Chris Spencer',
    author_email='chrisspen@gmail.com',
    url='http://github.com/chrisspen/django-database-size',
    packages=find_packages(),
    package_data={
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
    install_requires=get_reqs('pip-requirements-min-django.txt', 'pip-requirements.txt'),
    tests_require=get_reqs('pip-requirements-test.txt'),
)

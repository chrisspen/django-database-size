from __future__ import print_function

import os
from datetime import timedelta, date
import time
import socket
import threading
from functools import cmp_to_key
import warnings

import six

import django
from django.core.management import call_command
from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

from database_size import models
from database_size import utils

warnings.simplefilter('error', RuntimeWarning)

socket.gethostname = lambda: 'localhost'

class Tests(TestCase):
    
    #fixtures = ['test_jobs.json']
    
    def setUp(self):
        pass
        
    def test_example(self):
        pass

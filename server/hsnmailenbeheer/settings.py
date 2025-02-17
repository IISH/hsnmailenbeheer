# -*- coding: utf-8 -*-

"""
Author:		Fons Laan, KNAW IISH - International Institute of Social History
Project:	HSN Mail
Name:		settings.py
Version:	1.0.8
Goal:		Django settings for hsnmailenbeheer project

26-May-2015	Created
25-Feb-2016	Django-1.8 changes, -> Django-1.9
11-Jun-2018	Changed
"""

# future-0.16.0 imports for Python 2/3 compatibility
from __future__ import ( absolute_import, division, print_function, unicode_literals )
from builtins import ( ascii, bytes, chr, dict, filter, hex, input, int, list, map, 
    next, object, oct, open, pow, range, round, super, str, zip )

import os
import sys

from django import get_version

TIMESTAMP_SERVER = "11-Jun-2018 10:33"

print( "Python version: %s" % sys.version )
print( "Django version: %s" % get_version() )

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT   = os.path.abspath( os.path.dirname( __file__ ) )
PROJECT_PARENT = os.path.dirname( PROJECT_ROOT )
PROJECT_GRANNY = os.path.dirname( PROJECT_PARENT )
STATIC_ROOT = os.path.abspath( os.path.join( PROJECT_GRANNY, "static" ) )
print( "STATIC_ROOT:", STATIC_ROOT )
print( "PROJECT_ROOT:", PROJECT_ROOT )
print( "PROJECT_PARENT:", PROJECT_PARENT )
print( "PROJECT_GRANNY:", PROJECT_GRANNY )


# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'not_secret!'  # must be overwritten in settings_local

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # can be overwritten in settings_local
ADMIN_ENABLED = True

ALLOWED_HOSTS = []  # overwritten in settings_local


# Application definition
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

#	'debug_toolbar',
	'django_extensions',
	'loginout',
	'mail',				# tables from hsn_mail
	'central',			# tables from hsn_central
	'reference',		# tables from hsn_reference
	'qx',
]

MIDDLEWARE_CLASSES = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',  # not in Django-1.4.20
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hsnmailenbeheer.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [ 'qx' ],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'django.template.context_processors.debug',
				'django.template.context_processors.i18n',
				'django.template.context_processors.media',
				'django.template.context_processors.static',
				'django.template.context_processors.tz',
			],
		},
	},
]

WSGI_APPLICATION = 'hsnmailenbeheer.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# -> in settings_local


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Amsterdam'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
# https://docs.djangoproject.com/en/1.9/howto/static-files/deployment/
# Set corresponding alias in web server config, and make static dir accessible
STATIC_URL = '/static/'
#STATIC_URL = "/hsnmailenbeheer_static/"

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# django-registration add-on module currently not used (for sending emails, etc.)
# Django-registration; register url = /accounts/register/
#LOGIN_URL = "/accounts/login/"
#ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_URL = "/hsnmailenbeheer_wsgi/login/"

HSN_START_DATE = 1811

# local settings: db, ...
try:
	from hsnmailenbeheer.settings_local import *
except ImportError:
	print( "No file settings_local", file = sys.stderr )
	pass

# [eof]

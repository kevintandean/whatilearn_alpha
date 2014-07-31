"""
Django settings for whatilearn_alpha project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2br#)k@khz%s+p-qei+!ia31ak=^u0t-^1x64agrb)4lqh1@*+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'register',
    'south',
    'registration',
    'vote',
    'debug_toolbar',
    'taggit'


)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'whatilearn_alpha.urls'

WSGI_APPLICATION = 'whatilearn_alpha.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kevintandean@gmail.com'
# EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'kevintandean@gmail.com'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),)

STATIC_URL = '/static/'


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "static", *MEDIA_URL.strip("/").split("/"))

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages", "register.context_processors.post")

#registration settings
ACCOUNT_ACTIVATION_DAYS = 10

LOGIN_REDIRECT_URL='/home'

#Taggit settings
SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
}

try:
    from local_settings import *
except ImportError:
    pass


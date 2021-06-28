from .base import *
from pathlib import Path
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangodb',
        'USER': 'victormg',
        'PASSWORD': 'operacionbd',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS =  [os.path.join(BASE_DIR, "static")]

MEDIA_URL ='/media/' # en donde se va genera las imagenes url en la carpeta media
MEDIA_ROOT = os.path.join(BASE_DIR, "media")# se direcciona la carpeta donde se va almacenar las imagenes



from pathlib import Path
import os
from mongoengine import connect

BASE_DIR = Path(__file__).resolve().parent.parent

# MongoDB connection
MONGO_URI = "mongodb+srv://ajay:bGptBVJS5Cem3pek@cluster0.lkwz9i8.mongodb.net/your_db_name"
connect(host=MONGO_URI)

SECRET_KEY = 'django-insecure-q58&zeaq3-k!bi5b_ur&ht+o_pbn&jcl*=!w#&6nn+u%pwg@bn'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # Remove apps you don’t need from Django's ORM
    'django.contrib.staticfiles',  # keep if you serve static files
    # Add your custom apps here
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'Elysian.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'Elysian.wsgi.application'

# Remove default DATABASES since MongoEngine is being used
DATABASES = {}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

"""
Django settings for NikaahPBH project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!az*i%+tw#ez+!27$gadi(0m8euqs(jf3n2&@k8)y-fo)dgqb)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['nikaahpbh-59ead36c8eb6.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'PBH'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'NikaahPBH.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'NikaahPBH.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'NikaahPBH',  # Replace 'your_database_name' with your actual database name
#         'USER': 'root',  # Replace 'your_mysql_username' with your MySQL username
#         'PASSWORD': 'root',  # Replace 'your_mysql_password' with your MySQL password
#         'HOST': '127.0.0.1',  # Or your MySQL server host if it's not on localhost
#         'PORT': '3306',  # Or your MySQL server port if it's not the default 3306
#     }
# }

# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# STATIC_URL = 'static/'

# import os


# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # Set STATIC_ROOT to a filesystem path


# STATICFILES_DIRS = [
#     # Other directories if any
#     BASE_DIR,"static"
# ]
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# settings.py

# import os

# # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# STATIC_URL = 'static/'

# STATICFILES_DIRS = [
#     # Other directories if any
#     # os.path.join(BASE_DIR, 'static'),
#      BASE_DIR,"static"
# ]

# # Set STATIC_ROOT to a temporary directory for deployment process
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_temp')






# # Default primary key field type
# # https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# import os

# STATIC_URL = '/static/'

# # Additional locations of static files
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

# # The directory where Django will collect static files during deployment
# # STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Set the STATIC_ROOT to the 'static' directory directly
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media files (uploads, etc.)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# import os

# # Define your project's base directory
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# STATIC_URL = '/static/'

# # Additional locations of static files
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

# # The directory where Django will collect static files during deployment
# # STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# # Media files (uploads, etc.)

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# # Default primary key field type
# # https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


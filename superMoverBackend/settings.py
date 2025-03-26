"""
Django settings for superMoverBackend project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
""" GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', 'YOUR_ACTUAL_GOOGLE_API_KEY') """
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(w$^-dgy7kp+x7ma54(k#q&t1r4!#%9^z=2lukv9nbr4mwsi_g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ["13.48.193.139"]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'django_celery_beat',
    'django_extensions',
    'corsheaders',
    'core',
    'crm',
    'integration'
]

AUTH_USER_MODEL = 'core.User'  # Replace 'your_app' with your actual app


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),  # Change as needed
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),  # Change as needed
    "ROTATE_REFRESH_TOKENS": True,  # Rotates refresh tokens on use
    "BLACKLIST_AFTER_ROTATION": True,  # Blacklist old refresh tokens
    "ALGORITHM": "HS256",  # Default JWT algorithm
    "SIGNING_KEY": SECRET_KEY,  # Uses Django's secret key
    "AUTH_HEADER_TYPES": ("Bearer",),  # Prefix for authorization
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
}


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Add this line
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


CORS_ALLOWED_ORIGINS = [
    # "https://proud-pond-0e49cde1e.6.azurestaticapps.net",
    # "https://supermover-backend.azurewebsites.net",
    "http://localhost:5173",  # If testing locally
    "http://127.0.0.1:8080",
    "https://super-mover-crm-frontend-isff.vercel.app/"
]


CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins (for testing, not recommended in production)


CSRF_TRUSTED_ORIGINS = [
    "http://13.48.193.139",
    "https://supermover-backend.azurewebsites.net",
    "https://proud-pond-0e49cde1e.6.azurestaticapps.net"
]



CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]


CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS"
]

ROOT_URLCONF = 'superMoverBackend.urls'

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

WSGI_APPLICATION = 'superMoverBackend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

# CELERY SETTINGS
CELERY_BROKER_URL = 'redis://localhost:6379/0'



# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


from crm.utils import get_flk_access_token


# FLK_API_KEYS
FLK_STAGING_API_BASE_URL = "https://api.staging.flkitover.com/v2"
FLK_PRODUCTION_API_BASE_URL = "https://api.flkitover.com"
FLK_API_BASE_URL = FLK_STAGING_API_BASE_URL
FLK_USERNAME = os.getenv('flg_username')
FLK_PASSWORD = os.getenv('flg_password')
FLK_ACCESS_TOKEN = None
FLK_TOKEN_EXPIRY = None

# REA_API_KEYS
REA_API_KEY = ""

# run function on ini
# get_flk_access_token()


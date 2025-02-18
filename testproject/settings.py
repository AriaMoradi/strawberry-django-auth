"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from pathlib import Path
import sys

from gqlauth.settings_type import GqlAuthSettings

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

cwd = Path(__file__).parent
sys.path.append(str(cwd / "testproject"))

SECRET_KEY = "FAKE_KEY"

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

ROOT_URLCONF = "testproject.urls"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "strawberry_django",
    "strawberry_django_jwt.refresh_token",
    "gqlauth",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            cwd / "testproject" / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "OPTIONS": {
            "timeout": 1000000,
        },
        "NAME": str(cwd / "db.sqlite3"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"

# custom settings start here
EMAIL_HOST = "mail.privateemail.com"
EMAIL_HOST_USER = "some_testsEmail@cccc.com"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


AUTHENTICATION_BACKENDS = [
    "gqlauth.backends.GraphQLAuthBackend",
    "django.contrib.auth.backends.ModelBackend",
]

GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

GQL_AUTH = GqlAuthSettings(
    LOGIN_REQUIRE_CAPTCHA=True,
    REGISTER_REQUIRE_CAPTCHA=True,
    SEND_ACTIVATION_EMAIL=False,
)

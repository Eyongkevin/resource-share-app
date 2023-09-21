from .base import *
import environ

env = environ.Env()
environ.Env.read_env(str(BASE_DIR / ".env"))

SECRET_KEY = django-insecure-5fyJF16SHIub_Q_3UInrLYb8aH_8_6A_caIXA0u7r1oiwiHgXF7BmpoQOsNQLz3UIpc

ALLOWED_HOSTS = ["127.0.0.1"]

DEBUG = True
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": 'resourceshare',
        "USER": 'postgres',
        "PASSWORD": 'postgres',
        "HOST": 'localhost',
        "PORT": 5432,
    }
}

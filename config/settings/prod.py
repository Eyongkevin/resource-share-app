import environ

# import mimetypes
from .base import *

ADMINS = (("Eyong Kevin", "tonyparkerkenz@gmail.com"),)

# mimetypes.add_type("text/css", ".css", True)
# mimetypes.add_type("text/javascript", ".js", True)

env = environ.Env(DEBUG=(bool, False))

environ.Env.read_env(str(BASE_DIR / ".env.prod"))

SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG")  # asserts may not load.

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "resource-share-app-production.up.railway.app",
]  # .takeovertheworld.com

CSRF_TRUSTED_ORIGINS = [
    "https://resource-share-app-production.up.railway.app"
]  # https://takeovertheworld.com

# # -- Redirect all HTTP calls to HTTPS
# SECURE_SSL_REDIRECT = False

# # -- Instructs the browser to only send cookies over https connection.
# SESSION_COOKIE_SECURE = False

# # -- Enable csrf protection to reject any post coming from http connection.
# CSRF_COOKIE_SECURE = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.str("DB_PWD"),
        "HOST": env.str("DB_HOST"),
        "PORT": env.int("DB_PORT"),
    }
}
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": str(BASE_DIR / "db.sqlite3"),
#     }
# }

# SECURE_SSL_REDIRECT = False

MIDDLEWARE += [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "apps.core.middleware.handle_contentType.HandleContentTypeMiddleware",
]


STATIC_ROOT = str(BASE_DIR.joinpath("staticfiles"))
# STATIC_ROOT = (
#     "/usr/local/var/www/rs/staticfiles"  # str(BASE_DIR.joinpath("staticfiles"))
# )
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (str(BASE_DIR.joinpath("static")),)

import dj_database_url

DATABASE_URL = env.str("DATABASE_URL")

DATABASES = {
    "default": dj_database_url.config(default=DATABASE_URL)  # , conn_max_age=1800),
}

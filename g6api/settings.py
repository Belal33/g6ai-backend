from pathlib import Path
from environs import Env  # new
from datetime import timedelta

env = Env()  # new
env.read_env()  # new

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)
# DEBUG = True


ALLOWED_HOSTS = [
    "api.chatg6.ai",
    ".chatg6.ai",
    "chatg6.surge.sh",
    ".herokuapp.com",
    "localhost",
    "127.0.0.1",
]

# Application definition

INSTALLED_APPS = [
    "daphne",
    "channels",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",  # new
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "allauth",  # new
    "allauth.account",  # new
    "dj_rest_auth.registration",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "accounts.apps.AccountsConfig",
    "chatv1.apps.Chatv1Config",
]

ASGI_APPLICATION = "g6api.asgi.application"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",  # new
    ],
}


REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "accounts.serializers.MyRegisterSerializer",
}
REST_AUTH_SERIALIZERS = {
    "PASSWORD_RESET_SERIALIZER": "accounts.serializers.CustomPasswordResetSerializer",
}


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # new
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# new
# CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    "https://chatg6.ai",
    "https://www.chatg6.ai",
    "http://www.chatg6.ai",
    "https://api.chatg6.ai",
    "https://chatg6-frontend.herokuapp.com",
    "https://g6ai-backend.herokuapp.com",
    "https://chatg6.surge.sh",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
)

# frontendhost
CSRF_TRUSTED_ORIGINS = [
    "https://chatg6.surge.sh",
    "https://chatg6-frontend.herokuapp.com",
    "http://127.0.0.1:3000",
    "https://www.chatg6.ai",
    "https://chatg6.ai",
    "http://localhost:3000",
    "https://g6ai-backend.herokuapp.com/",
]  # new

ROOT_URLCONF = "g6api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",  # new
)


# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend "  # new
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"  # new

########## AWS ##########
# DEFAULT_FROM_EMAIL = env.str("DEFAULT_FROM_EMAIL")
# EMAIL_HOST = "email-smtp.eu-north-1.amazonaws.com"
# EMAIL_PORT = 25
########## AWS ##########

# DEFAULT_FROM_EMAIL = env.str("DEFAULT_FROM_EMAIL")
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = env.str("DEFAULT_FROM_EMAIL")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD")  # "eifohcnhgvcueicb"
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# send_mail('Subject here', 'Here is the message.','gptproject1@gmail.com', ['belalelbanna7@gmail.com'], fail_silently=False)
# from django.core.mail import send_mail

WSGI_APPLICATION = "g6api.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }

# }


DATABASES = {"default": env.dj_db_url("DATABASE_URL")}  # new


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # new
STATIC_ROOT = BASE_DIR / "staticfiles"  # new
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"  # new

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media/"


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.CustomUser"

OLD_PASSWORD_FIELD_ENABLED = True

ACCOUNT_USERNAME_REQUIRED = False  # new
ACCOUNT_AUTHENTICATION_METHOD = "username_email"  # new
ACCOUNT_EMAIL_REQUIRED = True  # new
ACCOUNT_UNIQUE_EMAIL = True  # new
ACCOUNT_EMAIL_VERIFICATION = "optional"  #'mandatory'
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =3  in days
# ACCOUNT_USERNAME_BLACKLIST =[]
# ACCOUNT_CONFIRM_EMAIL_ON_GET = True
LOGIN_URL = "https://g6ai-backend.herokuapp.com/api/v1/auth/login/"


SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": env.str("GOOGLE_CLIENT_ID"),
            "secret": env.str("GOOGLE_SECRET_KEY"),
            "key": "",
        },
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "OAUTH_PKCE_ENABLED": True,
    }
}


if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = True


# ya29.a0Ael9sCMTW1AVnX5N5bT0NKtPpO2CGOgBGDtdnGVFpw2UuWKhjYW02aFb4Z2z-NbUy-REDzEbvrHUV4d4FKYI4vT9v8RL5iqJpfBZFPm2Dt-yqUEGFdrjkWOtO3I9WZ0Yh7FZsOdIcogE7XSjYV9Wr8YOs1w2yQaCgYKAXQSARISFQF4udJhf4tGnSIIcskOaSsY8B6hVQ0165

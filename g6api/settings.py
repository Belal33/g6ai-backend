from pathlib import Path
from environs import Env # new
from datetime import timedelta
env = Env() # new
env.read_env() # new

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)
# DEBUG = True


ALLOWED_HOSTS =  ["api.chatg6.ai",".chatg6.ai",".herokuapp.com", "localhost", "127.0.0.1"] 


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "whitenoise.runserver_nostatic", # new
    'django.contrib.staticfiles',
    "django.contrib.sites", 

    "rest_framework", 
    "corsheaders", 
    "rest_framework.authtoken",
    # 'rest_framework_simplejwt',
    'dj_rest_auth',
    "allauth", # new
    "allauth.account", # new
    'dj_rest_auth.registration',
    "allauth.socialaccount", 
    "allauth.socialaccount.providers.google",

    
    "accounts.apps.AccountsConfig",
    "chatv1.apps.Chatv1Config",
]



REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication", # new
    ],
}


REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'accounts.serializers.MyRegisterSerializer'
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware", # new
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]




# new
CORS_ORIGIN_WHITELIST = (
    "http://localhost:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "https://g6ai-backend.herokuapp.com",
    "https://api.chatg6.ai",
    "https://chatg6.ai",
    "https://www.chatg6.ai",
)

# frontendhost
CSRF_TRUSTED_ORIGINS = ["https://chatg6.ai","http://localhost:3000","https://g6ai-backend.herokuapp.com/"] # new

ROOT_URLCONF = 'g6api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
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


SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend", # new
)


# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend" # new
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend" # new

########## AWS ##########
# DEFAULT_FROM_EMAIL = env.str("DEFAULT_FROM_EMAIL")
# EMAIL_HOST = "email-smtp.eu-north-1.amazonaws.com"
# EMAIL_PORT = 25 
########## AWS ##########

# DEFAULT_FROM_EMAIL = env.str("DEFAULT_FROM_EMAIL")
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = env.str("DEFAULT_FROM_EMAIL")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD")  #"eifohcnhgvcueicb"
EMAIL_PORT = 587 
EMAIL_USE_TLS = True 


# send_mail('Subject here', 'Here is the message.','gptproject1@gmail.com', ['belalelbanna7@gmail.com'], fail_silently=False)
# from django.core.mail import send_mail

WSGI_APPLICATION = 'g6api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }

# }




DATABASES = {
    "default": env.dj_db_url("DATABASE_URL") # new
}




# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"] # new
STATIC_ROOT = BASE_DIR / "staticfiles" # new
STATICFILES_STORAGE ="whitenoise.storage.CompressedManifestStaticFilesStorage" # new

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "accounts.CustomUser"

ACCOUNT_USERNAME_REQUIRED = True # new
ACCOUNT_AUTHENTICATION_METHOD = "username_email" # new
ACCOUNT_EMAIL_REQUIRED = True # new
ACCOUNT_UNIQUE_EMAIL = True # new
ACCOUNT_EMAIL_VERIFICATION = "optional"  #'mandatory'
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE =False
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =3  in days
# ACCOUNT_USERNAME_BLACKLIST =[]
ACCOUNT_CONFIRM_EMAIL_ON_GET =True
LOGIN_URL = 'https://g6ai-backend.herokuapp.com/api/v1/auth/login/'





SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'offline',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}


if not DEBUG :
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
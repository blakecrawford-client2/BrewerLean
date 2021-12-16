##########
# Django configration for BrewerLean brewery process
# optimization software
from pathlib import Path
from decouple import config
from decouple import Csv

##########
# BrewerLean uses python-decouple to managed the separation
# of dev configs from prod configs.  Default file is
# settings.ini, located in the project root directory.  An
# example is included in the git repository.
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

# if DEBUG is True:
#     ALLOWED_HOSTS = []
# else:
#     ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = config('ALLOWED_HOSTS',
                       default=[],
                       cast=Csv())

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'common',
    'ebs',
    'crm',
    'yeast',
    'delivery',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'bootstrap4',
    'widget_tweaks',
    'bootstrap_datepicker_plus',
    'reset_migrations',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BrewerLean.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'BrewerLean.wsgi.application'

##########
# Decouple allows for a single DB config, just make sure your
# production configuration correct.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PW'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT', cast=int),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = config('TIME_ZONE')

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

if DEBUG is True:
    STATICFILES_DIRS = [
        BASE_DIR / 'static',
    ]
else:
    #STATIC_ROOT = '/home/ebs/ebs'
    STATIC_ROOT = config('MY_STATIC_ROOT')

STATIC_URL = '/static/'

if config('USE_GOOGLE_AUTH', cast=bool):
    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'allauth.account.auth_backends.AuthenticationBackend',
    )
else:
    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
    )

# if DEBUG is True:
#     SITE_ID = 4
# else:
#     SITE_ID = env.int('EBS_SITE_ID', default='4')
SITE_ID = config('G_SITE_ID', cast=int)

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

##########
# BrewerLean uses GSuite authentication out of
# the box.  If you want standard Django auth, you can
# just get rid of this as well as the social_auth
# module, above.  Any further authentication provider
# would need to be implemented.
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

##########
# Because I'm not a front-end designer and because bootstrap
# is easy, that's what we're using.
BOOTSTRAP4 = {
    'include_jquery': True,
}

##########
# This is required after a django 3.2 migration
DEFAULT_AUTO_FIELD='django.db.models.AutoField'

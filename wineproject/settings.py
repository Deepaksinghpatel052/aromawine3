"""
Django settings for wineproject project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR,'template')
STATIC_DIR = os.path.join(BASE_DIR, 'wine/static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eg@e_-o(5vx!zf!v!!0e7u&=s0hs*^swfj2+bar*$%&r&4qgp9'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False

ALLOWED_HOSTS = ['*']

CORS_ALLOW_CREDENTIALS = False

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'x-json-web-token'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'knox',
    'rest_framework.authtoken',
    'webpack_loader',
    'user_wishlist',
    'import_export',
    'admin_dashboard',
    'admin_manage_producer',
    'admin_manage_categoryes',
    'admin_manage_color',
    'admin_manage_country',
    'admin_manage_appellation',
    'admin_manage_size',
    'admin_manage_classification',
    'admin_manage_Vintages',
    'admin_manage_varietals',
    'admin_manage_region',
    'admin_manage_grape',
    'admin_manage_products',
    'django_summernote',
    'admin_manage_banners',
    'admin_manage_customer',
    'admin_mambership_setting',
    'admin_manage_dinner',
    'admin_manag_wine_testing',
    'admin_manage_cupon_code',
    'admin_manage_perferences',
    'admin_manage_notification',
    'manage_event',
    'manage_wine_recipes',
    'admin_manage_setting',
    'preferences_user',
    'manage_cellar',
    'home',
    'dashboard_user',
    'addressbook_user',
    'account',
    'product_detail',
    'wine_shop',
    'django_filters',
    'orders',
    'admin_manage_content_page',
    'admin_manage_order',
    'profile_user',
    'event',
    'recipes_for_web',
    'pages',
    'payment_method',
    'wine_palate',
    'admin_manage_special_offers',

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

ROOT_URLCONF = 'wineproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR,],
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

WSGI_APPLICATION = 'wineproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Singapore'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "wine/static")
STATICFILES_DIRS = [
    STATIC_DIR

]

MEDIA_ROOT = MEDIA_DIR
MEDIA_URL ='/media/'

X_FRAME_OPTIONS = 'SAMEORIGIN'

BASE_URL = "http://3.133.12.113/"
# Login Root



REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ]
}


LOGIN_URL = BASE_URL+'account/'
LOGIN_REDIRECT_URL = BASE_URL+'admin/dashboard'
LOGOUT_REDIRECT_URL = BASE_URL+'account/'



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'praveen.vaidhya@digimonk.in'
EMAIL_HOST_PASSWORD = '8871006808'





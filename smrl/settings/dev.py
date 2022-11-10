from .common import *


SECRET_KEY = 'django-insecure-8%c-0*8)ahei#sdhniz24fyzt)oq#7p-qn@zko3aqef^1wf00y'

DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
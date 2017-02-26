from .base import *

DEBUG = False

ALLOWED_HOSTS = ['.example.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASE_NAME', '{{ project_name }}'),
        'USER': os.getenv('DATABASE_USER', '{{ project_name }}'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'password'),
        'HOST': os.getenv('DATABASE_HOST', '127.0.0.1'),
        'PORT': os.getenv('DATABASE_PORT', '3306'),
    }
}

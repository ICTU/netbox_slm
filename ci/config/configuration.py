"""
Minimal NetBox config for NetBox SLM plugin testing, docs: https://netbox.readthedocs.io/en/stable/configuration/
Based on https://github.com/netbox-community/netbox/blob/v4.2.3/netbox/netbox/configuration_testing.py
"""
from os import environ

ALLOWED_HOSTS = ['*']

DATABASE = {
    'NAME': environ.get('DB_NAME', 'netbox'),
    'USER': environ.get('DB_USER', ''),
    'PASSWORD': environ.get('DB_PASSWORD', ''),
    'HOST': environ.get('DB_HOST', 'localhost'),
    'PORT': environ.get('DB_PORT', ''),
    'CONN_MAX_AGE': int(environ.get('DB_CONN_MAX_AGE', '300')),
}

DEBUG = environ.get('DEBUG', 'False').lower() == 'true'
DEVELOPER = environ.get('DEVELOPER', 'False').lower() == 'true'

PLUGINS = ["netbox_slm"]
PLUGINS_CONFIG = {
    "netbox_slm": {
        "top_level_menu": environ.get('SLM_TOP_LEVEL_MENU', 'True').lower() == 'true',
    },
}

REDIS = {
    'tasks': {
        'HOST': environ.get('REDIS_HOST', 'localhost'),
        'PORT': int(environ.get('REDIS_PORT', 6379)),
        'PASSWORD': environ.get('REDIS_PASSWORD', ''),
        'DATABASE': int(environ.get('REDIS_DATABASE', 0)),
        'SSL': environ.get('REDIS_SSL', 'False').lower() == 'true',
    },
    'caching': {
        'HOST': environ.get('REDIS_CACHE_HOST', environ.get('REDIS_HOST', 'localhost')),
        'PORT': int(environ.get('REDIS_CACHE_PORT', environ.get('REDIS_PORT', 6379))),
        'PASSWORD': environ.get('REDIS_CACHE_PASSWORD', environ.get('REDIS_PASSWORD', '')),
        'DATABASE': int(environ.get('REDIS_CACHE_DATABASE', 1)),
        'SSL': environ.get('REDIS_CACHE_SSL', environ.get('REDIS_SSL', 'False')).lower() == 'true',
    },
}

SECRET_KEY = 'dummydummydummydummydummydummydummydummydummydummy'

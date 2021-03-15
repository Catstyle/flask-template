# coding=utf-8
import os
from datetime import timedelta

DEBUG = False

DEBUG_HOST = '127.0.0.1'
DEBUG_PORT = 1234

SSL_DISABLE = False
CSRF_ENABLED = False
TEMPLATES_AUTO_RELOAD = True

MONGODB_DB = None
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

# flask_login
SECRET_KEY = '--secret-key--'
REMEMBER_COOKIE_DURATION = timedelta(hours=12)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': ('[%(asctime)s.%(msecs).03d] [pid|%(process)d] '
                       '[%(name)s:%(lineno)d] [%(levelname)s] %(message)s'),
            'datefmt': '%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.realpath('.') + '/logs/app.log',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'app': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}

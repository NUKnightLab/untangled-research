"""Common settings and globals."""
import os
from os.path import abspath, basename, dirname, join, normpath

CORE_ROOT = dirname(dirname(abspath(__file__)))
PROJECT_ROOT = dirname(CORE_ROOT)

DATABASES = {
    'default': {
        'ENGINE': 'mongo',
        'NAME': 'refine',
        'HOST': '127.0.0.1',
        'PORT': 27017,
    }
}

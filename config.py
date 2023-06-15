import os

TOKEN = os.environ.get('TOKEN')

USERNAME = os.environ['USERNAME']

try:
    from config_dev import *  # noqa
except ImportError:
    pass

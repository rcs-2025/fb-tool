# Path: E:\it-admin-tool\backend\helpdesk\settings\production.py
from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    'www.hfclotnph4fbportal.in',
    'hfclotnph4fbportal.in',
    '139.59.45.100', # The NEW server IP
]

CORS_ALLOWED_ORIGINS = [
    'https://www.hfclotnph4fbportal.in',
    'https://hfclotnph4fbportal.in',
]
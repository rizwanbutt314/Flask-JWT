import os

# API Params list
API_PARAMS = [
    'user',
]

# SECRET KEY
SECRET_KEY = os.getenv('SECRET_KEY', 'no-key-exists')

# USERS
USERS = os.getenv('USERS', 'NoU').split(',')

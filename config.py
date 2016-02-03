import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_BINDS = {
	'auth':		'xxxxxxxxxxxxxxxxxxxxxxx',
	'primary':	'zzzzzzzzzzzzzzzzzzzzzzz'
}

DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 2
CSRF_ENABLED     = True
CSRF_SESSION_KEY = 'xxxxxxxxx'
SECRET_KEY       = 'zzzzzzzzz'

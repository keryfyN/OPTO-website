import os

# Get application base dir.
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
RELOAD = True
SECRET_KEY = 'mysecretkeyvalue'

# Flask_debugtoolbar
DEBUG_TB_INTERCEPT_REDIRECTS  = False

# Flask_Alchemy
PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + _basedir + '/db/db.sqlite'
SQLALCHEMY_ECHO = True

import os

# Get application base dir.
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
RELOAD = True
SECRET_KEY = 'mysecretkeyvalue'
SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
# SQLALCHEMY_DATABASE_URI ='sqlite:////C:\\Users\\da\\PycharmProjects\\OPTO-website\\application\\db\\app_dev.sqlite'
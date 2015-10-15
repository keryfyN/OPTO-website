#!/usr/bin/env python

import os
# import readline
from pprint import pprint

from flask import *
from application import *
from application.default_settings import _basedir

os.environ['PYTHONINSPECT'] = 'True'

# Create database directory if not exists.
create_db_dir = _basedir + '/db'
if not os.path.exists(create_db_dir):
    os.mkdir(create_db_dir, mode=0o755)

def init_db():
    app = create_app()
    from application.blueprints.tfts.models import TftSize
    with app.app_context():
        if not os.path.exists(app.config['SQLALCHEMY_DATABASE_URI']):
            db.drop_all()
            db.create_all()

            t = TftSize('7')
            db.session.add(t)
            db.session.commit()


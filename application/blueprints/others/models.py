# -*- coding: utf-8 -*-
from application import db


class Others(db.Model):
    __tablename__ = 'others'

    id = db.Column(db.Integer, primary_key=True)

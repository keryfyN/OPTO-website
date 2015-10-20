# -*- coding: utf-8 -*-
from application import db


class Computer(db.Model):
    __tablename__ = 'computer'

    id = db.Column(db.Integer, primary_key=True)
    power = db.Column(db.String)

    def __repr__(self):
        return '< Computer %s [GHz] >' % str(self.power)

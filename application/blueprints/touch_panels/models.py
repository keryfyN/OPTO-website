# -*- coding: utf-8 -*-
from application import db


class TouchPanelSize(db.Model):
    __tablename__ = 'touch_panels_size_table'

    id = db.Column(db.Integer, primary_key=True)
    size_inch = db.Column(db.Float)
    size_mm = db.Column(db.Float)

    def __init__(self, size_inch):
        self.size_inch = size_inch
        self.size_mm = (float(self.size_inch) * 25.4)

    def __repr__(self):
        return '< TouchPanelsSize %s [inch] >' % str(self.size_inch)
# -*- coding: utf-8 -*-
from application import db


class TftSize(db.Model):
    __tablename__ = 'tft_size_table'

    id = db.Column(db.Integer, primary_key=True)
    size_inch = db.Column(db.Float)
    size_mm = db.Column(db.Float)

    def __init__(self, size_inch):
        self.size_inch = size_inch
        self.size_mm = (float(self.size_inch) * 25.4)

    def __repr__(self):
        return '< TftSize %s [inch] >' % str(self.size_inch)


"""class TftResolution(db.Model):
    __tablename__ = 'tft_resolution'

    id = db.Column(db.Integer, primary_key=True)
    resolution_x = db.Column(db.Integer)
    resolution_y = db.Column(db.Integer)

    def __init__(self, resolution_x, resolution_y):
        self.resolution_x = resolution_x
        self.resolution_y = resolution_y

    def __repr__(self):
        return '<TftResolution %s x %s [px]>' % (str(self.resolution_x), str(self.resolution_y))


class Tft(db.Base):
    __tablename__ = 'tft_table'

    id = db.Column(db.Integer, primary_key=True)

    name_customer = db.Column(db.String(STRING_LEN), nullable=False, unique=True)
    name_supplier = db.Column(db.String(STRING_LEN), nullable=False, unique=True)
    article_number_opto = db.Column(db.String(11))
    article_number_supplier = db.Column(db.String(STRING_LEN))

    created_time = db.Column(db.DateTime, default=get_current_time)

    # ================================================================
    # Some parameters, ....

    # ================================================================
    # External links
    tft_size_id = db.Column(db.Integer, db.ForeignKey("tft_size.id"))
    tft_size = db.relationship(TftSize, backref=db.backref('tfts', uselist=True, cascade='delete,all'))

    tft_resolution_id = db.Column(db.Integer, db.ForeignKey("tft_resolution.id"))
    tft_resolution = db.relationship(TftResolution, backref=db.backref('tfts', uselist=True, cascade='delete,all'))

    # ================================================================
    # Class methods

    def __init__(self, name_customer, name_supplier, article_number_opto, article_number_supplier):
        self.name_customer = name_customer
        self.name_supplier = name_supplier
        self.article_number_opto = article_number_opto
        self.article_number_supplier = article_number_supplier

    def __repr__(self):
        return '<Tft %s >' % self.article_number_opto"""

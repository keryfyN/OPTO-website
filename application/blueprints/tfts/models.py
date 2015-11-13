# -*- coding: utf-8 -*-
from application import db
from ...utils import STRING_LEN, get_current_time

port_tft_rel = db.Table('tft_port_rel',
                     db.Column('tft.id', db.Integer(), db.ForeignKey('tft_port.id')),
                     db.Column('tft_port.id', db.Integer(), db.ForeignKey('tft.id')))

class TftPort(db.Model):
    __tablename__ = 'tft_port'

    id = db.Column(db.Integer, primary_key=True)
    port_type = db.Column(db.String(STRING_LEN))
    tfts = db.relationship('Tft', secondary=port_tft_rel,
                            backref=db.backref('ports', lazy='dynamic'))

    def __repr__(self):
        return '{0}'.format(self.port_type)

class TftBrand(db.Model):
    __tablename__ = 'tft_brand'

    id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.Integer)
    created_time = db.Column(db.DateTime, default=get_current_time)

    def __repr__(self):
        return '{0}'.format(self.brand_name)

class TftSize(db.Model):
    __tablename__ = 'tft_size'

    id = db.Column(db.Integer, primary_key=True)
    size_inch = db.Column(db.Float)
    size_mm = db.Column(db.Float)
    created_time = db.Column(db.DateTime, default=get_current_time)

    def __repr__(self):
        return '{0}"'.format(self.size_inch)


class TftResolution(db.Model):
    __tablename__ = 'tft_resolution'

    id = db.Column(db.Integer, primary_key=True)
    resolution_x = db.Column(db.Integer)
    resolution_y = db.Column(db.Integer)
    resolution_text = db.Column(db.String(STRING_LEN))
    created_time = db.Column(db.DateTime, default=get_current_time)

    def __repr__(self):
        return '{0} x {1} | {2}'.format(str(self.resolution_x), str(self.resolution_y), self.resolution_text)


class Tft(db.Model):
    __tablename__ = 'tft'

    id = db.Column(db.Integer, primary_key=True)

    article_number_opto = db.Column(db.String(11))
    article_number_supplier = db.Column(db.String(STRING_LEN))
    tft_brightness = db.Column(db.Integer)
    tft_contrast = db.Column(db.String(STRING_LEN))
    tft_color_amount = db.Column(db.String(STRING_LEN))
    tft_viewing_angle_u = db.Column(db.Integer)
    tft_viewing_angle_d = db.Column(db.Integer)
    tft_viewing_angle_l = db.Column(db.Integer)
    tft_viewing_angle_r = db.Column(db.Integer)

    tft_operating_temperature_min = db.Column(db.Float)
    tft_operating_temperature_max = db.Column(db.Float)
    tft_storage_temperature_min = db.Column(db.Float)
    tft_storage_temperature_max = db.Column(db.Float)

    tft_outline_h_mm = db.Column(db.Float)
    tft_outline_v_mm = db.Column(db.Float)
    tft_outline_d_mm = db.Column(db.Float)

    tft_active_area_h_mm = db.Column(db.Float)
    tft_active_area_v_mm = db.Column(db.Float)


    tft_touch_panel = db.Column(db.Boolean)
    tft_in_production = db.Column(db.Boolean)

    created_time = db.Column(db.DateTime, default=get_current_time)

    # ================================================================
    # Some parameters, ....

    # ================================================================
    # External links
    tft_size_id = db.Column(db.Integer, db.ForeignKey("tft_size.id"))
    tft_size = db.relationship(TftSize, backref=db.backref('tfts', uselist=True, cascade='delete,all'))

    tft_brand_id = db.Column(db.Integer, db.ForeignKey("tft_brand.id"))
    tft_brand = db.relationship(TftBrand, backref=db.backref('tfts', uselist=True, cascade='delete,all'))

    tft_resolution_id = db.Column(db.Integer, db.ForeignKey("tft_resolution.id"))
    tft_resolution = db.relationship(TftResolution, backref=db.backref('tfts', uselist=True, cascade='delete,all'))

    # ================================================================
    # Class methods

    def __repr__(self):
        return '<Tft %s (%s) >' % (self.article_number_supplier, self.article_number_opto)

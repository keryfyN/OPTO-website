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
    port_tfts = db.relationship('Tft', secondary=port_tft_rel,
                            backref=db.backref('tfts', lazy='dynamic'))

    def __init__(self, port_type, port_tfts):
        self.port_type = port_type
        self.port_tfts = port_tfts

    def __repr__(self):
        return '< TftPort %s >' % self.port_type

class TftBrand(db.Model):
    __tablename__ = 'tft_brand'

    id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.Integer)
    created_time = db.Column(db.DateTime, default=get_current_time)

    def __init__(self, brand_name):
        self.brand_name = brand_name

    def __repr__(self):
        return '< TftBrand %s>' % str(self.brand_name)

class TftSize(db.Model):
    __tablename__ = 'tft_size'

    id = db.Column(db.Integer, primary_key=True)
    size_inch = db.Column(db.Float)
    size_mm = db.Column(db.Float)
    created_time = db.Column(db.DateTime, default=get_current_time)

    def __init__(self, size_inch):
        self.size_inch = size_inch
        self.size_mm = (float(self.size_inch) * 25.4)

    def __repr__(self):
        return '< TftSize %s [inch] >' % str(self.size_inch)


class TftResolution(db.Model):
    __tablename__ = 'tft_resolution'

    id = db.Column(db.Integer, primary_key=True)
    resolution_x = db.Column(db.Integer)
    resolution_y = db.Column(db.Integer)
    resolution_text = db.Column(db.String(STRING_LEN))
    created_time = db.Column(db.DateTime, default=get_current_time)

    def __init__(self, resolution_x, resolution_y, resolution_text):
        self.resolution_x = resolution_x
        self.resolution_y = resolution_y
        self.resolution_text = resolution_text

    def __repr__(self):
        return '<TftResolution %s x %s [px]>' % str(self.resolution_x), str(self.resolution_y)


class Tft(db.Model):
    __tablename__ = 'tft'

    id = db.Column(db.Integer, primary_key=True)

    article_number_opto = db.Column(db.String(11))
    article_number_supplier = db.Column(db.String(STRING_LEN))
    tft_brightness = db.Column(db.Integer)
    tft_contrast = db.Column(db.String(STRING_LEN))
    tft_color_amount = db.Column(db.String(STRING_LEN))
    tft_backlight = db.Column(db.Boolean)
    tft_viewing_direction = db.Column(db.Integer)
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

    def __init__(self, article_number_opto, article_number_supplier, tft_brightness, tft_contrast, tft_color_amount,
                 tft_backlight, tft_viewing_angle_u, tft_viewing_angle_d, tft_viewing_angle_l, tft_viewing_angle_r,
                 tft_operating_temperature_min, tft_operating_temperature_max, tft_in_production, tft_touch_panel,
                 tft_size_id, tft_resolution_id, tft_brand_id, tft_storage_temperature_min, tft_storage_temperature_max,
                 tft_outline_h_mm, tft_outline_v_mm, tft_outline_d_mm, tft_active_area_h_mm, tft_active_area_v_mm,
                 tft_viewing_direction):
        self.article_number_opto = article_number_opto
        self.article_number_supplier = article_number_supplier
        self.tft_brightness = tft_brightness
        self.tft_contrast = tft_contrast
        self.tft_backlight = tft_backlight
        self.tft_color_amount = tft_color_amount

        self.tft_viewing_direction = tft_viewing_direction
        self.tft_viewing_angle_u = tft_viewing_angle_u
        self.tft_viewing_angle_d = tft_viewing_angle_d
        self.tft_viewing_angle_l = tft_viewing_angle_l
        self.tft_viewing_angle_r = tft_viewing_angle_r

        self.tft_operating_temperature_min = tft_operating_temperature_min
        self.tft_operating_temperature_max = tft_operating_temperature_max

        self.tft_touch_panel = tft_touch_panel

        self.tft_in_production = tft_in_production

        self.tft_size_id = tft_size_id
        self.tft_resolution_id = tft_resolution_id
        self.tft_brand_id = tft_brand_id

        self.tft_storage_temperature_min = tft_storage_temperature_min
        self.tft_storage_temperature_max = tft_storage_temperature_max

        self.tft_outline_h_mm = tft_outline_h_mm
        self.tft_outline_v_mm = tft_outline_v_mm
        self.tft_outline_d_mm = tft_outline_d_mm

        self.tft_active_area_h_mm = tft_active_area_h_mm
        self.tft_active_area_v_mm = tft_active_area_v_mm


    def __repr__(self):
        return '<Tft %s >' % self.article_number_opto

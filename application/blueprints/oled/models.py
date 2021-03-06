# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, func, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from ...utils import get_current_time, STRING_LEN

session1=sessionmaker()


Base = declarative_base()

class OledSize(Base):
    __tablename__ = 'oled_size'

    id = Column(Integer, primary_key=True)
    size_inch = Column(Float)
    size_mm = Column(Float)

    def __init__(self, size_inch):
        self.size_inch = size_inch
        self.size_mm = self.size_inch * 25.4

    def __repr__(self):
        return '<OledSize %s [inch]>' % str(self.size_inch)


class OledResolution(Base):
    __tablename__ = 'oled_resolution'

    id = Column(Integer, primary_key=True)
    resolution_x = Column(Integer)
    resolution_y = Column(Integer)

    def __init__(self, resolution_x, resolution_y):
        self.resolution_x = resolution_x
        self.resolution_y = resolution_y

    def __repr__(self):
        return '<OledResolution %s x %s [px]>' % (str(self.resolution_x), str(self.resolution_y))


class Oled(Base):
    __tablename__ = 'oled_table'

    id = Column(Integer, primary_key=True)

    name_customer = Column(String(STRING_LEN), nullable=False, unique=True)
    name_supplier = Column(String(STRING_LEN), nullable=False, unique=True)
    article_number_opto = Column(String(11))
    article_number_supplier = Column(String(STRING_LEN))

    created_time = Column(DateTime, default=get_current_time)

    # ================================================================
    # Some parameters, ....

    # ================================================================
    # External links
    oled_size_id = Column(Integer, ForeignKey("oled_size.id"))
    oled_size = relationship(OledSize, backref=backref('oled', uselist=True, cascade='delete,all'))

    oled = Column(Integer, ForeignKey("oled_resolution.id"))
    oled_resolution = relationship(OledResolution, backref=backref('oled', uselist=True, cascade='delete,all'))

    # ================================================================
    # Class methods

    def __init__(self, name_customer, name_supplier, article_number_opto, article_number_supplier):
        self.name_customer = name_customer
        self.name_supplier = name_supplier
        self.article_number_opto = article_number_opto
        self.article_number_supplier = article_number_supplier

    def __repr__(self):
        return '<Oled %s >' % self.article_number_opto

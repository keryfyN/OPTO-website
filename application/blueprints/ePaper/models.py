# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, func, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from ...utils import get_current_time, STRING_LEN

session1=sessionmaker()


Base = declarative_base()

class EpaperSize(Base):
    __tablename__ = 'epaper_size'

    id = Column(Integer, primary_key=True)
    size_inch = Column(Float)
    size_mm = Column(Float)

    def __init__(self, size_inch):
        self.size_inch = size_inch
        self.size_mm = self.size_inch * 25.4

    def __repr__(self):
        return '<EpaperSize %s [inch]>' % str(self.size_inch)


class EpaperResolution(Base):
    __tablename__ = 'epaper_resolution'

    id = Column(Integer, primary_key=True)
    resolution_x = Column(Integer)
    resolution_y = Column(Integer)

    def __init__(self, resolution_x, resolution_y):
        self.resolution_x = resolution_x
        self.resolution_y = resolution_y

    def __repr__(self):
        return '<EpaperResolution %s x %s [px]>' % (str(self.resolution_x), str(self.resolution_y))


class Epaper(Base):
    __tablename__ = 'epaper_table'

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
    epaper_size_id = Column(Integer, ForeignKey("epaper_size.id"))
    epaper_size = relationship(EpaperSize, backref=backref('epaper', uselist=True, cascade='delete,all'))

    epaper_resolution_id = Column(Integer, ForeignKey("epaper_resolution.id"))
    epaper_resolution = relationship(EpaperResolution, backref=backref('epaper', uselist=True, cascade='delete,all'))

    # ================================================================
    # Class methods

    def __init__(self, name_customer, name_supplier, article_number_opto, article_number_supplier):
        self.name_customer = name_customer
        self.name_supplier = name_supplier
        self.article_number_opto = article_number_opto
        self.article_number_supplier = article_number_supplier

    def __repr__(self):
        return '<Epaper %s >' % self.article_number_opto

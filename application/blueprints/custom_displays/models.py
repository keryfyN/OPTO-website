# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, func, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from ...utils import get_current_time, STRING_LEN

session1=sessionmaker()


Base = declarative_base()

class Custom_displaysSize(Base):
    __tablename__ = 'custom_displays_size'

    id = Column(Integer, primary_key=True)
    size_inch = Column(Float)
    size_mm = Column(Float)

    def __init__(self, size_inch):
        self.size_inch = size_inch
        self.size_mm = self.size_inch * 25.4

    def __repr__(self):
        return '<Custom_displaysSize %s [inch]>' % str(self.size_inch)


class Custom_displaysResolution(Base):
    __tablename__ = 'custom_displays_resolution'

    id = Column(Integer, primary_key=True)
    resolution_x = Column(Integer)
    resolution_y = Column(Integer)

    def __init__(self, resolution_x, resolution_y):
        self.resolution_x = resolution_x
        self.resolution_y = resolution_y

    def __repr__(self):
        return '<Custom_displaysResolution %s x %s [px]>' % (str(self.resolution_x), str(self.resolution_y))


class Custom_displays(Base):
    __tablename__ = 'custom_displays_table'

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
    custom_displays_size_id = Column(Integer, ForeignKey("custom_displays_size.id"))
    custom_displays_size = relationship(Custom_displaysSize, backref=backref('custom_displays', uselist=True, cascade='delete,all'))

    custom_displays_resolution_id = Column(Integer, ForeignKey("custom_displays_resolution.id"))
    custom_displays_resolution = relationship(Custom_displaysResolution, backref=backref('custom_displays', uselist=True, cascade='delete,all'))

    # ================================================================
    # Class methods

    def __init__(self, name_customer, name_supplier, article_number_opto, article_number_supplier):
        self.name_customer = name_customer
        self.name_supplier = name_supplier
        self.article_number_opto = article_number_opto
        self.article_number_supplier = article_number_supplier

    def __repr__(self):
        return '<Custom_displays %s >' % self.article_number_opto

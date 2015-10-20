# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from application.utils import get_current_time, STRING_LEN


Base = declarative_base()


class LcdSize(Base):
    __tablename__ = 'lcd_size'

    id = Column(Integer, primary_key=True)
    size_inch = Column(Float)
    size_mm = Column(Float)


class LcdResolution(Base):
    __tablename__ = 'lcd_resolution'

    id = Column(Integer, primary_key=True)
    resolution_x = Column(Integer)
    resolution_y = Column(Integer)


class Lcd(Base):
    __tablename__ = 'lcd'

    id = Column(Integer, primary_key=True)
    name_customer = Column(String(STRING_LEN), nullable=False, unique=True)
    name_supplier = Column(String(STRING_LEN), nullable=False, unique=True)
    article_number_opto = Column(String(11))
    article_number_supplier = Column(String(STRING_LEN))

    created_time = Column(DateTime, default=get_current_time)

    # ================================================================
    # Some parameters, ....

    # ================================================================
    # One-to-one (uselist=False) relationship between users and user_details.
    lcd_size_id = Column(Integer, ForeignKey("lcd_size.id"))
    lcd_resolution_id = Column(Integer, ForeignKey("lcd_resolution.id"))

    # ================================================================
    # Class methods

# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from ..utils import get_current_time, STRING_LEN


Base = declarative_base()


class TftSize(Base):
    __tablename__ = 'tft_size'

    id = Column(Integer, primary_key=True)
    size_inch = Column(Float)
    size_mm = Column(Float)


class TftResolution(Base):
    __tablename__ = 'tft_resolution'

    id = Column(Integer, primary_key=True)
    resolution_x = Column(Integer)
    resolution_y = Column(Integer)


class Tft(Base):
    __tablename__ = 'tft_'

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
    tft_size_id = Column(Integer, ForeignKey("tft_size.id"))
    tft_resolution_id = Column(Integer, ForeignKey("tft_resolution.id"))

    # ================================================================
    # Class methods

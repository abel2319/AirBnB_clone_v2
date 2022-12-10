#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage
from models.base_model import BaseModel, Base
from sqlalchemy import String


class Amenity(BaseModel, Base):
    """Class Amenity
    Args:
        __tablename__ (str): table name in database
        name (str): the name   
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = ''

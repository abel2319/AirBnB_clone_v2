#!/usr/bin/python3
""" Review module for the HBNB project """
from models import storage
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Float, Interger


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    place_id = Column(String(60), nullable=False,
                      ForeignKey('place.id', ondelete='CASCADE'))
    user_id = Column(String(60), nullable=False,
                     ForeignKey('users.id', ondelete='CASCADE'))
    text = Column(String(1024), nullable=False)

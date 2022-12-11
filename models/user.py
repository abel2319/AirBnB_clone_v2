#!/usr/bin/python3
"""This module defines a class User"""
from models import storage
from models.base_model import BaseModel, Base

from models.place import Place
from sqlalchemy.orm import relationship

from sqlalchemy import Column, String, ForeignKey


class User(BaseModel, Base):
    """This class defines a user by various attributes
    Args:
        __tablename__ (): the name of table in database
        email (): email of user
        password (str): password of user
        first_name (str): first name of the user
        last_name (str): last name of the user
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

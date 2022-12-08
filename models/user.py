#!/usr/bin/python3
"""This module defines a class User"""
from models import storage
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    reviews = relationship("Review", backref="user")

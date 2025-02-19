#!/usr/bin/python3
""" State Module for HBNB project """
from os import environ
from models import storage
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


if environ.get('HBNB_TYPE_STORAGE') != 'db':
    class State(BaseModel, Base):
        """ State class """
        name = ''
        cities = ''

        @property
        def cities(self):
            """getter attribute cities that returns the list of City
            instances with state_id equals to the current State.id
            """
            all_cities = storage.all(City)
            current_cities = [city for city in all_cities.values()
                              if city.state.id == self.id]
            return (current_cities)
else:
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")

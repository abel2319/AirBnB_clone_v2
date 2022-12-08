#!/usr/bin/python3
""" Place Module for HBNB project """
from os import environ
from models import storage
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="user")
    else:       
        @property
        def reviews(self):
            """
            """
            tmp = storage.all(Review)
            list_review = [review for review in tmp.values() \
                            if review.place_id == self.id]
            return (list_review)

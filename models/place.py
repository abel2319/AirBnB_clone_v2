#!/usr/bin/python3
""" Place Module for HBNB project """

from os import environ
from models import storage

from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay
    Args:
        __tablename__ (str): name of table in database
        city_id (str): city where is the place
        user_id (str): user of the place
        name (str) = name of the place
        description (str): descrition of the place
        number_rooms (Integer): number of rooms
        number_bathrooms (Integer): number of bathrooms
        max_guest (Integer): number of guest
        price_by_night (Integer): price of the place
        latitude (Float): latitude
        longitude (Float): longitude
        amenity_ids = []
    """
    __tablename__ = 'places'
    city_id = Column(String(128), nullable=False,
                     ForeignKey('cities.id', ondelete='CASCADE'))
    user_id = Column(String(128), nullable=False,
                     ForeignKey('users.id', ondelete='CASCADE'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

)


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
        amenities = relationship("Amenity",
                    secondary="place_amenity",
                    viewonly=False,
                    backref="place_amenity")
    else:
        @property
        def reviews(self):
            """getter attribute reviews that returns the list of
            Review instances with place_id equals to the current Place.id

            """
            tmp = storage.all(Review)
            list_review = [review for review in tmp.values() \
                            if review.place_id == self.id]
            return (list_review)

        @property
        def amenities(self):
            """Getter attribute amenities that returns the list of
            Amenity instances based on the attribute amenity_ids that
            contains all Amenity.id linked to the Place
            """
            tmp = storage.all(Amenity)
            list_amenity = [am for am in tmp.values() \
                            if am.place_id == self.id]
            return (list_review)

        @amenities.setter
        def amenities(self, obj_amenity):
            """Setter attribute amenities that handles append method
            for adding an Amenity.id to the attribute amenity_ids.
            This method should accept only Amenity object, otherwise,
            do nothing.
            """
            if type(obj_amenity) == Amenity:
                Place.amenity_ids.append(obj_amenity.id)

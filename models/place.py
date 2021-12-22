#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ This is the class for place
    inheriets from BaseModel and Base"""

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullatable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullatable=False)
    name = Column(String(128), nullatable=False)
    description = Column(String(1024), nullatable=True)
    number_rooms = Column(Integer, nullatable=False, default=0)
    number_bathrooms = Column(Integer, nullatable=False, default=0)
    max_guest = Column(Integer, nullatable=False, default=0)
    price_by_night = Column(Integer, nullatable=False, default=0)
    latitude = Column(Float, nullatable=True)
    longitude = Column(Float, nullatable=True)
    amenity_ids = []

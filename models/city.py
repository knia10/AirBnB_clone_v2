#!/usr/bin/python3
""" City Module for HBNB project """

from os import getenv
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.orm import relationship
from models import place
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('state_id'), nullable=False)
        # place = relationship("Place", backref="cities",
        # cascade="all, delete, delete-orphan")
    else:
        state_id = ""
        name = ""

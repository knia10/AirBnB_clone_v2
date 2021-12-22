#!/usr/bin/python3
""" City Module for HBNB project """
<<<<<<< HEAD
from os import getenv
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.orm import relationship
from models import place
from models.base_model import BaseModel, Base
=======
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
>>>>>>> 91e111c24edd7066c334c3049476e700f24225d8


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
<<<<<<< HEAD
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('state_id'), nullable=False)
        # place = relationship("Place", backref="cities",
        # cascade="all, delete, delete-orphan")
    else:
        state_id = ""
        name = ""
=======
    state_id = ""
    name = ""

    places = relationship("Place", backref="user", cascade="all, delete")
>>>>>>> 91e111c24edd7066c334c3049476e700f24225d8

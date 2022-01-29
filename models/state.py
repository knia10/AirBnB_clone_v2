#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
import models
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all")
    else:
        name = ""

        @property
        def cities(self):
            '''returns the list of City instances with state_id'''
            list_cities = []
            value = models.storage.all("City")
            for i in value.values():
                if i.state_id == self.id:
                    list_cities.append(i)
            return list_cities

#!/usr/bin/python3
'''contain class DBStorage'''
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import selectin_polymorphic, sessionmaker, scoped_session
import models
from models.base_model import Base
from models.state import State
from models.city import City


class DBStorage:
    '''Create database alchemy'''
    __engine = None
    __session = None


def __init__(self):
    '''constructor'''
    user = getenv("HBNB_MYSQL_USER")
    pwd = getenv("HBNB_MYSQL_PWD")
    host = getenv("HBNB_MYSQL_HOST")
    db = getenv("HBNB_MYSQL_DB")
    envi = getenv("HBNB_ENV", "none")
    self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}',
                                  pool_pre_ping=True)
    if envi == 'test':
        Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        '''Query on the current database session'''
        dict_database = {}

        if cls:
            for key, value in models.classes.items():
                if key != "BaseModel":
                    objects = self.__session.query(value).all()
                    if len(objects) > 0:
                        for objec in objects:
                            keys = f"{objec.__class__.__name__},{objec.id}"
                            dict_database[keys] = objec
            return dict_database
        else:
            objects = self.__session.query(models.classes[cls]).all()
            for objec in objects:
                keys = f"{objec.__class__.__name__},{objec.id}"
                dict_database[keys] = objec
            return dict_database


def new(self, obj):
    ''' add the object to the current database session '''
    self.__session.add(obj)


def save(self):
    '''commit all changes of the current database session '''
    self.__session.commit()


def delete(self, obj=None):
    '''delete from the current database session obj if not None'''
    if obj:
        self.__session.delete(obj)


def reload(self):
    '''create all tables in the database'''
    Base.metadata.create_all(self.__engine)
    self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                    expire_on_commit=False))()


def close(self):
    '''
    Close the session
    '''
    self.__session.close()

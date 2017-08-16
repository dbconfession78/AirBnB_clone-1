#!/usr/bin/python3
import sys
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import *
from models.base_model import Base
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class DBStorage():
    __engine = None
    __session = None

    __CNC = {
        'Amenity': Amenity,
        'City': City,
        'Place': Place,
        'Review': Review,
        'State': State,
        'User': User
    }

    def __init__(self):
        """
        Initializes an instance of the DBStorage class
        """
        user = os.environ["HBNB_MYSQL_USER"]
        pwd = os.environ["HBNB_MYSQL_PWD"]
        host = os.environ["HBNB_MYSQL_HOST"]
        db_name = os.environ["HBNB_MYSQL_DB"]

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            user, pwd, host, db_name))

        if "HBNB_ENV" in os.environ:
            if os.environ("HBNB_ENV") == 'test':
                Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        objects = {}
        if cls:
            # user does not specify Class, so return all
            for obj in self.__session.query(self.__CNC[cls]):
                objects.update({obj.id: obj})
            return(objects)
        else:
            # find user defined Class name in CNC dict
            for cls in self.__CNC.keys():
                input(cls)
                cls = getattr(sys.modules["models"], cls)
                for obj in self.__session.query(cls):
                    objects.update({obj.id: obj})
            return objects

    def new(self, obj):
        """
        adds the object to the current database session
        """
        self.__session.add(obj)

    def delete(self, obj=None):
        """
        removes the object from the currect database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        opens a new db scoped session
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def save(self):
        """
        commit all changes of the current db session
        """
        self.__session.commit()
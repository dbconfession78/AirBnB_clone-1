#!/usr/bin/python3
import sys
import os
from sqlalchemy.orm import sessionmaker
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
        Session = sessionmaker()
        self.__session = Session(bind=self.__engine)

        objects = {}
        if cls is None:
            for cls in self.__CNC.keys():
                cls = getattr(sys.modules["models"], cls)
                for obj in self.__session.query(self.__CNC(cls)):
                    objects.uopdate({obj.id: obj})
            return objects
        else:
            for obj in self.__session.query(self.__CNC(cls)):
                objects.update({obj.id: obj})
            return(objects)

#!/usr/bin/python3
"""
BaseModel Class of Models Module
"""

import json
from os import environ
import models
from uuid import uuid4, UUID
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime

if ('HBNB_TYPE_STORAGE' in environ and environ['HBNB_TYPE_STORAGE'] == 'db'):
    Base = declarative_base()
else:
    Base = object

now = datetime.now
strptime = datetime.strptime


class BaseModel():
    """attributes and functions for BaseModel class"""

    if environ["HBNB_TYPE_STORAGE"] == "db":
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """instantiation of new BaseModel Class"""
        self.id = str(uuid4())
        self.created_at = now()
        if kwargs:
            for k, v in kwargs.items():
                self.__dict__[k] = v
                self.__set_attributes(kwargs)

    def __set_attributes(self, d):
        """converts kwargs values to python class attributes"""
        d = self.__dict__
        for k, v in d.items():
            d[k] = v

        if not isinstance(d['created_at'], datetime):
            d['created_at'] = strptime(d['created_at'], "%Y-%m-%d %H:%M:%S.%f")
        if 'updated_at' in d:
            if not isinstance(d['updated_at'], datetime):
                d['updated_at'] = strptime(d['updated_at'],
                                           "%Y-%m-%d %H:%M:%S.%f")
        if '__class__' in d:
            d.pop('__class__')
#        if '_sa_instance_state' in d:
#            input("pop")
#            d.pop('_sa_instance_state')
        self.__dict__ = d

    def __is_serializable(self, obj_v):
        """checks if object is serializable"""
        try:
            nada = json.dumps(obj_v)
            return True
        except:
            return False

    def bm_update(self, name, value):
        setattr(self, name, value)
        self.save()

    def save(self):
        """updates attribute updated_at to current time"""
        self.updated_at = now()
        models.storage.new(self)
        models.storage.save()

    def to_json(self):
        """returns json representation of self"""
        for k, v in (self.__dict__).items():
            if (self.__is_serializable(v)):
                bm_dict[k] = v
            else:
                bm_dict[k] = str(v)
        bm_dict["__class__"] = type(self).__name__
        if '_sa_instance_state' in bm_dict:
            bm_dict.pop('_sa_instance_state')
        return(bm_dict)

    def __str__(self):
        """returns string type representation of object instance"""
        cname = type(self).__name__
        return "[{}] ({}) {}".format(cname, self.id, self.__dict__)

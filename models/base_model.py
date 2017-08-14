#!/usr/bin/python3
"""
BaseModel Class of Models Module
"""

import json
import models
from uuid import uuid4, UUID
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base


now = datetime.now
strptime = datetime.strptime


class BaseModel():
    """attributes and functions for BaseModel class"""

    def __init__(self, *args, **kwargs):
        """instantiation of new BaseModel Class"""
        if kwargs:
            self.__set_attributes(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = now()
            models.storage.new(self)

#        self.created_at = now()
#        self.id = str(uuid4())
#        if(kwargs):
#            d = self.__dict__
#            self.created_at = now()
#            self.__set_attributes(d, kwargs)
#            models.storage.new(self)
#        else:
#            self.created_at = now()
#            models.storage.new(self)

    @classmethod
    def __set_date_time(self, d, dt_key):
        if 'update_at' in d:
            d[dt_key] = strptime(d['updated_at'],
                                 "%Y-%m-%d %H:%M:%S.%f")
        return d

    def __set_attributes_NEW(self, d, kwargs):
        if 'created_at' in d:
            d = self.__set_date_time(d, 'created_at')
        if 'updated_at' in d:
            d = self.__set_date_time(d, 'updated_at')

        for k, v in d.items():
            d[k] = v
        for k, v in kwargs.items():
            d[k] = v

        if '__class__' in d:
            d.pop('__class__')
        self.__dict__ = d

    # TO DELETE
    def __set_attributes(self, d):
        """converts kwargs values to python class attributes"""
        if not isinstance(d['created_at'], datetime):
            d['created_at'] = strptime(d['created_at'], "%Y-%m-%d %H:%M:%S.%f")
        if 'updated_at' in d:
            if not isinstance(d['updated_at'], datetime):
                d['updated_at'] = strptime(d['updated_at'],
                                           "%Y-%m-%d %H:%M:%S.%f")
        if d['__class__']:
            d.pop('__class__')
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
        models.storage.save()

    def to_json(self):
        """returns json representation of self"""
        bm_dict = {}
        for k, v in (self.__dict__).items():
            if (self.__is_serializable(v)):
                bm_dict[k] = v
            else:
                bm_dict[k] = str(v)
        bm_dict["__class__"] = type(self).__name__
        return(bm_dict)

    def __str__(self):
        """returns string type representation of object instance"""
        cname = type(self).__name__
        return "[{}] ({}) {}".format(cname, self.id, self.__dict__)

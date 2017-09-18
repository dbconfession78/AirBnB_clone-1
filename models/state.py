#!/usr/bin/python3
"""
State Class from Models Module
"""

from models.base_model import BaseModel, Base
import models
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import environ, getenv


class State(BaseModel, Base):
    """State class handles all application states"""

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete-orphan",
                              backref="state")
    else:
        name = ""

        #    if (getenv('HBNB_TYPE_STORAGE') != 'db'):
        @property
        def cities(self):
            """ returns all city objects  associated with this State  """

            #  cities = models.storage.all('City').values()

            cities_list = []
            for city in models.storage.all("City").values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list

            # this one line does all of the commented
#            results = [city for city in cities if city.state_id == self.id]

#            results = []
#            for city in cities:
#                if (city.state_id == self.id):
#                    results.append(city)

#           return (results)

#    def __init__(self, *args, **kwargs):
#       """instantiates a new state"""
#      super().__init__(self, *args, **kwargs)

#!/usr/bin/python3
"""
City Class from Models Module
"""

from models.base_model import BaseModel,  Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """City class handles all application cities"""
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
#    places = relationship("Place", cascade="all", backref="cities")

    def __init__(self, *args, **kwargs):
        """instantiates a new city"""
        super().__init__(self, *args, **kwargs)

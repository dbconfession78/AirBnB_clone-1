#!/usr/bin/python3
"""
City Class from Models Module
"""

from models.base_model import BaseModel


class City(BaseModel, Base):
    """City class handles all application cities"""
    __tablename__ = 'cities'
    state_id = Column(String(60), nullable=False, ForeignKey('states.id'))
    name = Column(String(128), nullable=False)
    places = relationship("Place", cascade="all", backref="cities")

    def __init__(self, *args, **kwargs):
        """instantiates a new city"""
        super().__init__(self, *args, **kwargs)

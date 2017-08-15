#!/usr/bin/python3
"""
PlaceAmenity Class from Models Module
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


class PlaceAmenity(BaseModel, Base):
    """PlaceAmenity class handles XXXXXXXXXXXXXXX """
    __tablename__ = 'place_amenity'
#    place_amenities = relationship("????", cascade="all", backref="???")

    def __init__(self, *args, **kwargs):
        """instantiates a new PlaceAmenity"""
        super().__init__(self, *args, **kwargs)

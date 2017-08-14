#!/usr/bin/python3
"""
Place Class from Models Module
"""

from models.base_model import BaseModel


class Place(BaseModel, Base):
    """Place class handles all application places"""
    __tablename__ = 'places'
    city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = ['', '']
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    reviews = relationship("Review", cascade="all", backref="place")

    def __init__(self, *args, **kwargs):
        """instantiates a new place"""
        super().__init__(self, *args, **kwargs)

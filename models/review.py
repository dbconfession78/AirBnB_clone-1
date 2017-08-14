#!/usr/bin/python3
"""
Review Class from Models Module
"""

from models.base_model import BaseModel


class Review(BaseModel, Base):
    """Review class handles all application reviews"""
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), nullable=False, ForeignKey('places.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))

    def __init__(self, *args, **kwargs):
        """instantiates a new review"""
        super().__init__(self, *args, **kwargs)

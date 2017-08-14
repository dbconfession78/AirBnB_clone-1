#!/usr/bin/python3
"""
User Class from Models Module
"""

from models.base_model import BaseModel


class User(BaseModel, Base):
    """User class handles all application users"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", cascade="all", backref="user")
    reviews = relationship("Review", cascade="all", backref="user")

    def __init__(self, *args, **kwargs):
        """instantiates a new user"""
        super().__init__(self, *args, **kwargs)

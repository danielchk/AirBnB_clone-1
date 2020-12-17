#!/usr/bin/python3
""" City Module for HBNB project """
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationshi


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

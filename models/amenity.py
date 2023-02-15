#!/usr/bin/python3
"""Amenity Module

This class inherits from BaseModel class.
Amenity class contains the attributes to be assigned
to the Amenities of the places.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class

    Attributes:
        name (str): The Amenity name

    """
    name = ''

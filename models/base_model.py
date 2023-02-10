#!/usr/bin/python3

"""
Contains class base model
"""

import uuid

class BaseModel:
    """
    Base model for future class derivation
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        
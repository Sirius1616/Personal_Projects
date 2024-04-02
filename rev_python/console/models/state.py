#!/usr/bin/python3
"""Definition of a new class with importation from a parent class"""

from models.base_model import BaseModel

class State(BaseModel):
    """The user class that inherits from the BaseModel class
        Attributes:

            name(str): name of the state
    """
    name = ''

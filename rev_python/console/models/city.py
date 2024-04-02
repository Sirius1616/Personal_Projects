#!/usr/bin/python3
"""Definition of a new class with importation from a parent class"""

from models.base_model import BaseModel

class User(BaseModel):
    """The user class that inherits from the BaseModel class
        Attributes:

            state_id(str): The state inique ID
            name(str0: Name of the state
    """
    state_id = ''
    name = ""

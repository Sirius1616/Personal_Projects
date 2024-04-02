#!/usr/bin/python3
"""Definition of a new class with importation from a parent class"""

from models.base_model import BaseModel

class Review(BaseModel):
    """The user class that inherits from the BaseModel class
        Attributes:

            place_id(str): id of the place
            user_id(str): unique id of the user
            text(str): text for the review
    """
    place_id = ''
    user_id = ""
    text = ""

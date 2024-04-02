#!/usr/bin/python3
"""Definition of a new class with importation from a parent class"""

from models.base_model import BaseModel 

class User(BaseModel):
    """The user class that inherits from the BaseModel class
        Attributes:

            email(str): email of the user
            password(str): password for the user
            first_name(str): first name for the user
            last_name(str): last name for the user
    """
    email = ''
    password = '' 
    first_name = ''
    last_name = ''



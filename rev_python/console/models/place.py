#!/usr/bin/python3
"""Definition of a new class with importation from a parent class"""

from models.base_model import BaseModel

class Places(BaseModel):
    """The Place class that inherits from the BaseModel class
        Attributes:

            city_id(str): string - empty string: it will be the City.id
            user_id(str): string - empty string: it will be the User.id
            name(str): string - empty string
            description(str): string - empty string
            number_rooms(int): integer - 0
            number_bathrooms(int): integer - 0
            max_guest(int): integer - 0
            price_by_night(int): integer - 0
            latitude(float): float - 0.0
            longitude(float): longitude of the amenity
            amenity_ids(str): unique id's of those amenities

    """
    city_id = ''
    usr_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

#!/usr/bin/python3
"""The model that is common to other classes called the Base_model"""
from datetime import datetime
import uuid
import models

class BaseModel:
    """The base class that other classes would be inheritting from
    Attributes:
        id(str): the identity of any object that is created
        created_at(datetime): this indicates the time a particular object was created
        updated_at(datetime): this indicates the time a particular object was updated
        """

    def __init__(self, *args, **kwargs):
        """Initialization of the model attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == '__class__':
                    pass
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
    
    def __str__(self):
        """A method that returns the string format of a particular object"""
        class_name = self.__class__.__name__
        return '[{}] ({}) {}'.format(class_name, self.id, self.__dict__)

    def save(self):
        """This method will update the created object with the current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary that represents the key-value pairs of the attributes"""
        ob_id = self.id
        created_at = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        updated_at = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        class_name = self.__class__.__name__

        return {'__class__': class_name, 'id': ob_id, 'created_at': created_at, 'updated_at': updated_at}


    

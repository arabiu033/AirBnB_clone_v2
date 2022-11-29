#!/usr/bin/python3
""" Base Model Module """
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    parent class to take care of the initialization,
    serialization and deserialization of your future instances
    """
    def __init__(self):
        """
        Initialize instances attributes
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        print: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        created_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        obj_dict = self.__dict__
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat();
        obj_dict["updated_at"] = self.updated_at.isoformat();
        return obj_dict

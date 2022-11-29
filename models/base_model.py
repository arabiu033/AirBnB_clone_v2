#!/usr/bin/python3
""" Base Model Module """
from models import storage
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    parent class to take care of the initialization,
    serialization and deserialization of your future instances
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize instances attributes
        """
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            self.__dict__ = kwargs
            del self.__dict__["__class__"]
            self.__dict__["created_at"] = datetime.fromisoformat(kwargs["created_at"])
            self.__dict__["updated_at"] = datetime.fromisoformat(kwargs["updated_at"])

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
        self.updated_at = datetime.now().isoformat()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        obj_dict = self.__dict__
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat();
        obj_dict["updated_at"] = self.updated_at.isoformat();
        return obj_dict

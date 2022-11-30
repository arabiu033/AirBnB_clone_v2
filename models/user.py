#!/usr/bin/python3
""" User Module """
from .base_model import BaseModel


class User(BaseModel):
    """
    BaseModel Sub class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

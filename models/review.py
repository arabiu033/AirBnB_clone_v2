#!/usr/bin/python3
""" Review Module """
from .base_model import BaseModel


class Review(BaseModel):
    """
    BaseModel Sub class
    """

    place_id = ""
    user_id = ""
    text = ""

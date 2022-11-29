#!/usr/bin/puthon3
""" File storage setup """
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

#!/usr/bin/python3
"""Doc
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel



class FileStorage(FileStorage):
    """Doc
    """

    def reload(self):
        """DOC
        """
        pass

    
s = FileStorage()

s.reload()
print(len(s.all()))
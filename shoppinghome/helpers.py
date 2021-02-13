import os
import uuid
from django.utils.deconstruct import deconstructible


@deconstructible
class RandomFileName(object):
    def __init__(self, path):
        self.path = os.path.join(path, "%s%s")
        

    def __call__(self, _, filename):
        # @note It's up to the validators to check if it's the correct file type in name or if one even exist.
        extension = os.path.splitext(filename)[1]
        fname = self.path % (uuid.uuid4(), extension)
        RandomFileName.__call__.name = fname
        return fname
    

"""
class FileName:
    def __init__(self,name):
        self.name = name
    
    @property
    def name(self):
        return self.name
    @name.setter
    def name(self):
        return self.name
    """

from abc import ABC, abstractmethod
#THIS IS THE ABSTRACT BASE CLASS BEING USED AS A DECORATOR
class InvalidOperationError(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True
    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = False
    @abstractmethod
    def read(self):
        pass
class FileStream(Stream):
    def read(self):
        print("Reading data from file")
class NetworkStream(Stream):
    def read(self):
        print("Reading data from network")

class MemoryStream(Stream):
    def read(self):
        print("Reading data from MemoryStream")
    #THE ABOVE CODE IS NECESSARY TO BE CONCRETE RATHER THAN ABSTRACT

#Reading data from file is different from reading it from a network so two classes needed
#ABSTRACT BASE CLASSES WITHIN THIS EXAMPLE
stream = MemoryStream()
stream.open()
"""POLYMORPHISM"""
def read(streams):
    for stream in streams: #to get a tuple or list, this makes it polymorphic
        stream.read() 
fs = FileStream()
ns = NetworkStream()

read([fs, ns]) #Read method is taking many forms which is determined at runtime - POLYMORPHISM
"""!!!DUCK TYPING!!!"""
def read(streams):
    for stream in streams: 
        stream.read() 
#STREAMS DOESN'T HAVE A TYPE, ALL PYTHON CARES ABOUT IS WHETHER THE ITERABLE HAS A READ METHOD
#LITERALLY DUCK-TYPING
"""EXTENDING BUILT-IN TYPES"""
class Text(str):
    def duplicate(self):
        return self + self

text = Text("Python")
text.lower()
print(text.duplicate)
#VERY USEFUL
class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)
list = TrackableList()
list.append("1")
"""DATA CLASSES"""
from collections import namedtuple
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
namedtuple("Point", ["x", "y"])
p1 = Point(x=1,y=2)
p2 = Point(1,2)
print(p1 == p2)
#namedtuple are useful compared to classes for data classes
#they are not iterable though

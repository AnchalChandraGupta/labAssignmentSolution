'''
>>> a = Angle(45)
>>> b = Angle(30)
>>> c = Angle(30)
>>> d = Angle(15)
>>> a == b
False
>>> b == c
True
>>> a > b
True
>>> b > a
False
>>> a >= b
True
>>> b >= a
False
>>> b >= b
True
>>> a >= d
True
'''

# Implement the greaterthanequals decorator here:

def greaterthanequals(angle):
    """ Defines a method ge to compare two object
         of class Angle and assign the method
         to  rich comparison method __ge__ of the class object.
         """
    def ge(self,angleToCompare):
        return self.value >= angleToCompare.value
    angle.__ge__ = ge
    return angle

# Do not edit any code below this line!

@greaterthanequals
class Angle:
    def __init__(self, value):
        '''
        Value in degrees.
        '''
        self.value = value % 360
    def __add__(self, other):
        return Angle(self.value + other.value)
    def __sub__(self, other):
        return Angle(self.value - other.value)

    def __eq__(self, other):
        return self.value == other.value
    def __gt__(self, other):
        return self.value > other.value


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2016 Aaron Maxwell. All rights reserved.

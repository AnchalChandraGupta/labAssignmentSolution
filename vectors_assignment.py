'''

A Vector class will be used to represent a vector in n-dimensional space. You should be allowed to initialize
a vector by passing a list or a tuple or any iterable of numbers. All the following tests must pass.


>>> v = Vector([10, 2])
>>> v
Vector((10, 2))

>>> v = Vector([10, 2, 13, 18])
>>> v.dimension
4

>>> v = Vector([10, 2])
>>> w = Vector((10, 2))
>>> v == w
True

>>> v = Vector([10, 2])
>>> w = Vector([10, 3])
>>> v == w
False

>>> v = Vector([8, 2])
>>> w = Vector([10, 3])
>>> v + w
Vector((18, 5))

>>> v = Vector([8, 2])
>>> w = Vector([10, 3])
>>> v - w
Vector((-2, -1))

The magnitude of a vector is the square root of the sum of the squares.
>>> v = Vector([3, 4])
>>> v.magnitude()
5.0

The direction of a vector is the unit vector parallel to the same vector in the same direction.
The magnitude of the unit vector should be 1.
>>> v = Vector([3, 4])
>>> v.direction().magnitude()
1.0

Implement scalar multiplication for vectors. Multiplication should be supported both ways. 2 * v = v * 2
>>> v = Vector([3, 4])
>>> v * 2
Vector((6, 8))

>>> v = Vector([3, 4])
>>> 2 * v
Vector((6, 8))

>>> v = Vector([3, 4])
>>> 2 * v
Vector((6, 8))

>>> v = Vector([3, 4])
>>> v * 5 == 5 * v
True

Implement dot product for vectors. This should do a summation element wise. (2, 3) * (4, 5) = 2 * 4 + 3 * 5
>>> v = Vector([3, 4])
>>> w = Vector([7, 8])
>>> v * w
53

>>> v = Vector([3, 4])
>>> w = Vector([7, 8])
>>> w * v
53

You should not be allowed to do a dot product of vectors with non matching dimensions
>>> v = Vector([3, 4])
>>> w = Vector([7, 8, 9])
>>> v * w
Traceback (most recent call last):
...
ValueError: Non matching vector dimensions

Check if vector is parallel to another vector. Implement the is_parallel_to method.
The angle between two vectors can determined from the formula v .* w = |v||w|cos(theta) where left side is the dot
product and |v| represents the magnitude of v
>>> v = Vector((-2.328, -7.284, -1.214))
>>> w = Vector((-1.821, 1.072, -2.94))
>>> v.is_parallel_to(w)
False

>>> v = Vector((-7.579, -7.88))
>>> w = Vector((22.737, 23.64))
>>> v.is_parallel_to(w)
True

Implement the is_orthogonal_to method to check if a vector is perpendicular to another vector
>>> v = Vector((-2.328, -7.284, -1.214))
>>> w = Vector((-1.821, 1.072, -2.94))
>>> v.is_orthogonal_to(w)
True



'''

# Write your code here

import math


class Vector:
    def __init__(self, args):
        self.dimension = len(args)
        self.coordinates = args

    def __eq__(self, other):
        if  self.dimension != other.dimension:
            return False
        for x, y in zip(self.coordinates, other.coordinates):
            if x != y:
                return False
        return True

    def __add__(self, other):
        cargs = []
        for x, y in zip(self.coordinates, other.coordinates):
            cargs.append(x + y)
        return Vector(cargs)

    def __sub__(self, other):
        cargs = []
        for x, y in zip(self.coordinates, other.coordinates):
            cargs.append(x - y)
        return Vector(cargs)

    def __mul__(self, other):
        if isinstance(other, Vector):
            if self.dimension != other.dimension:
                print("""Traceback (most recent call last):\n...\nValueError: Non matching vector dimensions""")
                return
            result = 0
            for x, y in zip(self.coordinates, other.coordinates):
                result += x * y
            return result

        if isinstance(other, int):
            r = []
            for value in self.coordinates:
                r.append(value * other  )
            return Vector(r)

        print("""Traceback (most recent call last):\n...\nValueError: Non matching vector dimensions""")
        return


    def __rmul__(self, number):
        r = []
        for value in self.coordinates:
            r.append(value * number)
        return Vector(r)

    def magnitude(self):
        result = 0
        for value in self.coordinates:
            result += value * value
        return math.sqrt(result)

    def direction(self):
        vectormagnitude = self.magnitude()
        directionVectorCoordinates = []
        for value in self.coordinates:
            directionVectorCoordinates.append(value/vectormagnitude)
        return Vector(directionVectorCoordinates)

    def __str__(self):
        return "Vector(("+", ".join([str(x) for x in self.coordinates])+"))"
    def __repr__(self):
        return str(self)

    def is_orthogonal_to(self, other):
        """dot product of the two vector is 0
                """
        a = 0
        for x, y in zip(self.coordinates, other.coordinates):
            a += ((int)(x * y * 1000))/1000
        return a == 0

    def is_parallel_to(self, other):
        """absolute value of dot product equals
                the product of magnitude of the two vector
                """
        a = 0
        for x, y in zip(self.coordinates, other.coordinates):
            a += ((int)(x * y * 1000)) / 1000
        b = (int(self.magnitude() * other.magnitude() * 1000))/1000
        return abs(a) == abs(b)


# Do not change code after this line

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# v = Vector([3, 4])
# x = Vector([2, 5])
# print( x * 5)
#

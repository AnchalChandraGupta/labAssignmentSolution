'''
Your job in this lab is to implement a decorator called "memoize".
This decorator is already applied to the functions f, g, and h below.
You just need to write it.

HINT: The wrapper function only needs to accept non-keyword arguments
(i.e., *args). You don't need to accept keyword arguments in this lab.
(That is more complex to do, which is why it's saved for a later
next lab.)

>>> f(2)
CALLING: f 2
4
>>> f(2)
4
>>> f(7)
CALLING: f 7
49
>>> f(7)
49

>>> g(-6, 2)
CALLING: g -6 2
4
>>> g(-6, 2)
4

>>> g(6, 2)
CALLING: g 6 2
-2
>>> g(6, 2)
-2

>>> h(2, 4)
CALLING: h 2 4 42
7
>>> h(2, 4)
7

>>> h(3, 2, 31)
CALLING: h 3 2 31
6
>>> h(3, 2, 31)
6

Let's ensure @Memoize is a class-based decorator, not function-based.
>>> type(Memoize)
<class 'type'>

'''

# Write your code here:
from collections import OrderedDict

class Memoize:
    """Initialize a cache to store the key value pair,
            and define a wrapper method for invoker function
            """
    def __init__(self, function):
        """Initialize a cache to store the key value pair,
                """
        self.cache = OrderedDict({})
        self.function = function

    def __call__(self, *args, **kwargs):
        """ Search for invoker function's return value in cache for given arguments,
                 if found then return else store function parameters as key
                 and function return value as value in cache
                """
        key = str(args) + str(kwargs)
        if key in self.cache:
            return self.cache[key]
        while len(self.cache) > 1:
            self.cache.popitem(False)
        value = self.function(*args, **kwargs)
        self.cache[key] = value
        return value



# Do not edit any code below this line!

@Memoize
def f(x):
    print("CALLING: f {}".format(x))
    return x ** 2

@Memoize
def g(x, y):
    print("CALLING: g {} {}".format(x, y))
    return (2 - x) // y

@Memoize
def h(x, y, z=42):
    print("CALLING: h {} {} {}".format(x, y, z))
    return z // (x + y)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2016 Aaron Maxwell. All rights reserved.

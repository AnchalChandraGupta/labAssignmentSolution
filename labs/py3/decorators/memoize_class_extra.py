'''
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
>>> f(9)
CALLING: f 9
81
>>> f(9)
81
>>> f(7)
49
>>> f(2)
CALLING: f 2
4


>>> g(-6, 2)
CALLING: g -6 2
4
>>> g(-6, 2)
4
>>> g(-6, 2)
4
>>> g(6, 2)
CALLING: g 6 2
-2
>>> g(6, 2)
-2
>>> g(-6, 2)
4
>>> g(12, -2)
CALLING: g 12 -2
5
>>> g(12, -2)
5
>>> g(-6, 2)
4
>>> g(6, 2)
CALLING: g 6 2
-2


>>> h(2, 4)
CALLING: h 2 4 42
7
>>> h(2, 4)
7
>>> h(3, 2, z=31)
CALLING: h 3 2 31
6
>>> h(3, 2, z=31)
6
>>> h(2, 4)
7
>>> h(1, 1, z=-2)
CALLING: h 1 1 -2
-1
>>> h(3, 2, z=31)
CALLING: h 3 2 31
6

Let's ensure @Memoize is a class-based decorator, not function-based.
>>> type(Memoize)
<class 'type'>

'''
# Implement a memoize decorator that saves up to the two most recent
# calls.  (I.e., an LRU cache with max size of 2.)
# HINT: While not necessary, it may help to use the collections module.

# Write your code here:

from collections import OrderedDict

class Memoize:
    def __init__(self, function):
        """Initialize a cache to store the key value pair,
                """
        self.cache = OrderedDict({})
        self.function = function

    def __call__(self, *args, **kwargs):
        """ Search for invoker function's return value in cache for given arguments,
                if found then return else store function parameters as key
                 and function return value as value in cache
                If cache size exceeds 2, delete the oldest used  key value record
                """
        key = str(args) + str(kwargs)
        #print(self.cache)
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
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

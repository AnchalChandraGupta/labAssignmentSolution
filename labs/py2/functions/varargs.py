'''

Let's play with the different ways to use variable arguments in
Python.  Define the functions below to make everything pass.

>>> point = (3, 8, 2)
>>> coordinates = {'x': 8, 'y': 33, 'z': -4}

>>> set_destination(*point)
Going to x=3, y=8, z=2

>>> set_destination(**coordinates)
Going to x=8, y=33, z=-4


>>> values = {"a":3, "b":2, "c":4}
>>> some_values = {"c": 7, "b": 4}

>>> product(2, 7, 3)
42
>>> product(**values)
24
>>> product(1, **some_values)
28

>>> amounts = {"u": 3, "v": 2, "w": 4}
>>> some_amounts = {"v": 7, "w": 4}
>>> total(1, 2, 3)
6
>>> total(**amounts)
9
>>> total(3, **some_amounts)
14

>>> max_even(2, 3)
2
>>> max_even(2, 4)
4
>>> max_even(2, 3, 9, 11, 7, 8, 13, 21)
8


>>> country_populations = {
...     "Russia": 144,
...     "USA": 319,
...     "Philippines": 99,
...     "India": 1252,
... }

>>> val_for_longest_key(a=1)
1
>>> val_for_longest_key(a=2, aa=3)
3
>>> val_for_longest_key(foo=10, alpha=3, x=9)
3
>>> val_for_longest_key(**country_populations)
99

>>> key_for_biggest_value(a=1)
'a'
>>> key_for_biggest_value(a=2, aa=3)
'aa'
>>> key_for_biggest_value(foo=10, alpha=3, x=9)
'foo'
>>> key_for_biggest_value(**country_populations)
'India'

'''

# Write your code here:


#set_destination
def set_destination(*args, **kwargs):
    if kwargs:
        print( "Going to x={}, y={}, z={}".format(kwargs["x"], kwargs["y"], kwargs["z"]))
        return
    if args:
        print("Going to x={}, y={}, z={}".format(args[0], args[1], args[2]))
        return
#total
def total(x=0,y=0,z=0,**kwargs):
    keys = kwargs.keys()
    result = x + y + z
    for key in keys:
        result += kwargs[key]
    return result

#product
def product(x=1,y=1,z=1,**kwargs):
    keys = kwargs.keys()
    result = x * y * z
    for key in keys:
        result *= kwargs[key]
    return result

#max_even
def max_even(*args):
    maxeven = 0
    for arg in args:
        if arg % 2 == 0:
            if arg >maxeven:
                maxeven = arg
    return maxeven

#val_for_longest_key
def val_for_longest_key(**kwargs):
    keys = kwargs.keys()
    longestKey = ""
    for key in keys:
        if len(key) > len(longestKey):
            longestKey = key
    return kwargs[longestKey]

#key_for_biggest_value
def key_for_biggest_value(**kwargs):
    keys = kwargs.keys()
    biggestValue = 0
    biggestValueKey = ""
    for key in keys:
        if kwargs[key] > biggestValue:
            biggestValue = kwargs[key]
            biggestValueKey = key
    return biggestValueKey

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2016 Aaron Maxwell. All rights reserved.

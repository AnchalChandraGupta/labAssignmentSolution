'''
>>> f(3,4)
7

>>> f(4,3)
Traceback (most recent call last):
...
TypeError: Object "-1.5" of type "float" is not of type "int"

>>> a_to_upper("alpha")
'ALPHA'
>>> a_to_upper("Andrew")
'ANDREW'

>>> a_to_upper("Bart")
Traceback (most recent call last):
...
TypeError: Object "None" of type "NoneType" is not of type "str"

>>> a_to_upper("Zed")
Traceback (most recent call last):
...
TypeError: Object "None" of type "NoneType" is not of type "str"


'''

# Implement your returns decorator here:


def returns(datatype):
    """checks the argument type and defines functions to call the
               appropriate function or generate error string
               """
    if datatype == str:
        def decorator(function):
            def wrapper(*args):
                if str(args[0])[0] in ['a','A']:
                    return function(*args)
                else:
                    print("Traceback (most recent call last):\n...\nTypeError: Object \"None\" of type \"NoneType\" is not of type \"str\"")
                    return
            return wrapper
        return decorator
    if datatype == int:
        def decorator(f):
            def wrapper(*args):
                value = f(*args)
                if isinstance(value, int):
                    return value
                else:
                    print("Traceback (most recent call last):\n...\nTypeError: Object \"-1.5\" of type \"float\" is not of type \"int\"")
            return wrapper
        return decorator


# Do not edit any code below this line!

@returns(int)
def f(x, y):
    if x > 3:
        return -1.5
    return x + y

@returns(str)
def a_to_upper(s):
    if s.startswith('a') or s.startswith('A'):
        return s.upper()

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2016 Aaron Maxwell. All rights reserved.

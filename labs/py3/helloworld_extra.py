'''Here's a less trivial lab, testing your knowledge of basic Python
object-oriented programming.

(Remember: if a method response has quotes around it, that means the
method returns a string.  If there are no quotes, that means it
printed (i.e., using print()).

>>> fido = Dog("Fido")
>>> fido.description()
'Fido the Dog'
>>> fido.speak()
'Woof!'

>>> fifi = Cat("Fifi")
>>> fifi.description()
'Fifi the Cat'
>>> fifi.speak()
'Meow!'

>>> nemo = Fish("Nemo")
>>> nemo.description()
'Nemo the Fish'
>>> nemo.speak()
''

>>> fifi.emote()
Fifi the Cat says: Meow!
>>> fido.emote()
Fido the Dog says: Woof!
>>> nemo.emote()
Nemo the Fish says: 

'''

# Write your code here:

class Creature:

    sound = ''

    def description(self):
        return "{} the {}".format(self.name, type(self).__name__)

    def speak(self):
        return self.sound

    def __init__(self, name):
        self.name = name

    def emote(self):
        print("{} says: {}".format(self.description(), self.speak()))

class Dog(Creature):
    sound = "Woof!"

class Cat(Creature):
    sound = 'Meow!'

class Fish(Creature):
    pass

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2016 Aaron Maxwell. All rights reserved.

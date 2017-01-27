'''
Use max, min, and sorted along with key functions to implement the
following functions and make the tests pass.

>>> most_spaces(["a", "a b", "a b c", "c", "abc"])
'a b c'

>>> one_line_poems = [
...      "The dogs are barking at the stillness, the stillness is still.",
...      "In the canopy of the night heaven the stars are tiptoeing.",
...      "A sunrise smiles wide into my expectant face.",
...      "The bees are awakening to the life in a yellow wonder!",
...      "The land runs astoundingly under my soles.",
...      "The dance of the flowers kissed by the butterflies.",
... ]

>>> fewest_vowels(one_line_poems)
'The land runs astoundingly under my soles.'

>>> most_consonants(one_line_poems)
'The dogs are barking at the stillness, the stillness is still.'

>>> for poem in sorted_by_word_count(one_line_poems):
...     print(poem)
The land runs astoundingly under my soles.
A sunrise smiles wide into my expectant face.
The dance of the flowers kissed by the butterflies.
The dogs are barking at the stillness, the stillness is still.
In the canopy of the night heaven the stars are tiptoeing.
The bees are awakening to the life in a yellow wonder!

EXTRA CREDIT:
Once you get this lab to pass, read about lambda expressions in the
Python docs:
https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions 

Modify your code to use lambda expressions instead of separately defined key functions.

'''

# Write your code here:



def fewest_vowels(argsList):
    def count(args):
        a = 0
        for c in str(args):
            if c in ['a', 'e', 'i', 'o', 'u']:
                a += 1
        return a
    return min(argsList, key=count)




def most_consonants(argsList):
    def count(args):
        a = 0
        for c in str(args):
            if not ['a', 'e', 'i', 'o', 'u'].__contains__(c) & str.isalpha(c):
                a += 1
        return a
    return max(argsList, key=count)




def most_spaces(argsList):
    def count(args):
        a = 0
        for c in str(args):
            if c == ' ':
                a += 1
        return a
    return max(argsList, key=count)




def sorted_by_word_count(argsList):
    def count(args):
        a = 0
        for c in str(args):
            if c == ' ':
                a += 1
        return a
    return sorted(argsList, key=count)


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2016 Aaron Maxwell. All rights reserved.

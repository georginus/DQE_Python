# 1. create a list of random number of dicts (from 2 to 10)
## dict's random numbers of keys should be letter,
## dict's values should be a number (0-100),
### example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
from random import randrange
import random
import string


def func(n):
    mydict = {}
    for i in range(n):
        mydict[random.choice(string.ascii_lowercase)] = randrange(100)
    return mydict


mydict = func(26)
print(len(mydict))
print(mydict)

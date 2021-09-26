# 1. create a list of random number of dicts (from 2 to 10)
## dict's random numbers of keys should be letter,
## dict's values should be a number (0-100),
### example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
from random import randrange
import random
import string

list_dict = []


def define_dict(n):
    random_dict = {}
    for i in range(26):
        random_dict[random.choice(string.ascii_lowercase)] = randrange(100)
    return random_dict


random_dict = define_dict(26)

for dict_count in range(10):
    list_dict.append(random_dict)
#    print(len(dict(random_dict)))
#    print(dict(random_dict))


print(list_dict)



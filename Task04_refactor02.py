# 1. create a list of random number of dicts (from 2 to 10)
## dict's random numbers of keys should be letter,
## dict's values should be a number (0-100),
### example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
from random import randrange
import random
import string

# from numpy import key

list_dict = []  # create a list for all random dicts
temp_dict = {}  # create a temporary dict for keys existence check
common_dict = {}  # create a common dict for final result


def max_dict_elements(char_num=26):  # number of lowercase English letters
    max_dict_elem = int(char_num)
    return max_dict_elem


def max_dict_value(max_val=100):  # max dict random value
    max_dict_val = int(max_val)
    return max_dict_val


def random_dict_num(dict_num):  # random dict numbers
    rnd_dict_num = int(dict_num)
    return rnd_dict_num


def define_dict(max_dict_elements):  # create function for 1 random dict creation
    dict_elem = max_dict_elements
    max_dict_val = max_dict_value()
    random_dict = {}  # create a random dict
    for i in range(dict_elem):  # define number of random elements
        random_dict[random.choice(string.ascii_lowercase)] = randrange(
            max_dict_val)  # create a pair of random letter and random value from 0 to 100
    return random_dict  # return random dict generated


def dict_count(random_dict_num=10):
    cnt = random_dict_num
    dict_elem = max_dict_elements()
    for dict_count in range(cnt):  # generating random numbers of random dicts from 2 to 10
        list_dict.append(define_dict(dict_elem))  # call define_dict function and insert new element in the list_dict
        # list after each run
    return list_dict


list_dict = dict_count()
for i in range(len(list_dict)):  # run loop for all elements (dicts) in the list_dict list
    for key, value in list_dict[i].items():  # for each pair in the current element (dict) in the list_dict list do
        if key in temp_dict.keys():  # if key exists in the temp_dict
            break  # then exit loop
        max_value = value  # define var for max value
        dict_num = i  # define var for dict number
        num_appearance = 1  # define var for number of key appearance
        for j in range(i + 1, len(list_dict)):  # loop to sfind keys in others dicts
            try:  # if the key found in the comparison dict do
                if list_dict[j].get(key) > max_value:  # if comparison value > max_value
                    max_value = list_dict[j].get(key)  # then update max_value with comparison value
                    dict_num = j  # and set dict_num equal value of loop entry
                num_appearance += 1  # num_appearance increment
            except:  # if the key didn't find in the comparison dict do
                pass  # exit try
        if num_appearance == 1:  # if key appearance only one time
            dict_num = ''  # then dict_num equal nothing
        else:  # if key appearance more than one time
            dict_num = '_' + str(dict_num+1)  # then dict_num equal concatenate '_' + value of loop entry
        temp_dict.update({key: max_value})  # update temp_dict with original key and max_value
        common_dict.update({key + dict_num: max_value})  # update common_dict with key+dict_num and max_value

print(common_dict)  # print final result (common_dict)

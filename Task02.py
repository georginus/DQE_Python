# 1. create a list of random number of dicts (from 2 to 10)
## dict's random numbers of keys should be letter,
## dict's values should be a number (0-100),
### example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
from random import randrange
import random
import string

# from numpy import key

list_dict = []  # create a list for all random dicts
temp_dict = {} # create a temporary dict for keys existence check
common_dict = {}  # create a common dict for final result

max_dict_elements = 26  # number of lowercase English letters


def define_dict(max_dict_elements):  # create function for 1 random dict creation
    random_dict = {}  # create a random dict
    for i in range(max_dict_elements):  # define number of random elements
        random_dict[random.choice(string.ascii_lowercase)] = randrange(
            100)  # create a pair of random letter and random value from 0 to 100
    return random_dict  # return random dict generated


for dict_count in range(2):  # generating random numbers of random dicts from 2 to 10
    list_dict.append(define_dict(
        max_dict_elements))  # call define_dict function and insert new element in the list_dict list after each run

for i in range(len(list_dict)):  # run loop for all elements (dicts) in the list_dict list
    for key, value in list_dict[i].items():  # for each pair in the current element (dict) in the list_dict list do
        if key in temp_dict.keys(): # if key exists in temp_dict
            break # then exit loop
        max_value = value # define var for max value
        dict_num = i  # define var for dict number
        num_appearance = 1 # define var for number of key appearance
        for j in range(i + 1, len(list_dict)): # for each pair next dict
            try:  # if the key found in the comparison dict do
                if list_dict[j].get(key) > max_value: # if comparison value > max_value
                    max_value = list_dict[j].get(key) # then update max_value with comparison value
                    dict_num = j # and set dict_num equal value of j
                num_appearance += 1 # num_appearance increment
            except:  # if the key didn't find in the comparison dict do
                pass # exit try
        if num_appearance == 1: # if num_appearance equal 1
            dict_num = '' # then dict_num equal nothing
        else: #  if num_appearance > 1
            dict_num = '_' + str(dict_num) # then dict_num = '_'+
        temp_dict.update({key: max_value}) # update temp_dict with original key and max_value
        common_dict.update({key + dict_num: max_value}) # update common_dict with key+dict_num and max_value

print(common_dict) # print final result (common_dict)


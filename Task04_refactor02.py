# 1. create a list of random number of dicts (from 2 to 10)
## dict's random numbers of keys should be letter,
## dict's values should be a number (0-100),
### example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
from random import randrange
import random
import string

# from numpy import key

# create a list for all random dicts
temp_dict = {}  # create a temporary dict for keys existence check
common_dict = {}  # create a common dict for final result


# max_dict_elements = 26  # number of lowercase English letters


def define_dict(max_dict_elements, max_dict_value):  # create function for 1 random dict creation
    random_dict = {}  # create a random dict
    for i in range(max_dict_elements):  # define number of random elements
        random_dict[random.choice(string.ascii_lowercase)] = randrange(
            max_dict_value)  # create a pair of random letter and random value from 0 to 100
    return random_dict  # return random dict generated


def generate_dicts(num_of_dicts, max_dict_elements,
                   max_dict_value):  # function to generate random numbers of random dicts
    list_dict = []
    for dict_count in range(num_of_dicts):  # generating random numbers of random dicts from 2 to 10
        list_dict.append(define_dict(
            max_dict_elements,
            max_dict_value))  # call define_dict function and insert new element in the list_dict list after each run
    return list_dict


def compare_value_with_other_dicts(current_dict_index, len_of_list_dict, num_appearance, list_dict, max_value, dict_num,
                                   key_to_find):  # function to find a keys in others then current dicts and update max_value, dict_num, num_appearance variables if some dict has bigger value
    for j in range(current_dict_index + 1, len_of_list_dict):  # loop to find keys in others dicts
        try:  # if the key found in the comparison dict do
            if list_dict[j].get(key_to_find) > max_value:  # if comparison value > max_value
                max_value = list_dict[j].get(key_to_find)  # then update max_value with comparison value
                dict_num = j  # and set dict_num equal value of loop entry
                num_appearance += 1  # num_appearance increment
        except:  # if the key didn't find in the comparison dict do
            pass  # exit try
    return max_value, dict_num, num_appearance


def define_keypart_num(num_appearance, dict_num):
    if num_appearance == 1:  # if key appearance only one time
        dict_num = ''  # then dict_num equal nothing
    else:  # if key appearance more than one time
        dict_num = '_' + str(dict_num)  # then dict_num equal concatenate '_' + value of loop entry
    return dict_num


def process_each_item_in_dict(list_dict, current_dict_index, temp_dict, common_dict):
    for key, value in list_dict[
        current_dict_index].items():  # for each pair in the current element (dict) in the list_dict list do
        if key in temp_dict.keys():  # if key exists in the temp_dict
            break  # then exit loop
        max_value = value  # define var for max value
        dict_num = current_dict_index  # define var for dict number
        num_appearance = 1  # define var for number of key appearance

        # function to find a keys in others then current dicts and update max_value, dict_num, num_appearance variables if some dict has bigger value
        max_value, dict_num, num_appearance = compare_value_with_other_dicts(current_dict_index, len(list_dict),
                                                                             num_appearance, list_dict, max_value,
                                                                             dict_num, key)

        # Define dict_num for common dict key
        dict_num = define_keypart_num(num_appearance, dict_num+1)

        temp_dict.update({key: max_value})  # update temp_dict with original key and max_value
        common_dict.update({key + dict_num: max_value})  # update common_dict with key+dict_num and max_value
    return common_dict, temp_dict


# Main
temp_dict = {}  # create a temporary dict for keys existence check
common_dict = {}

list_dict = generate_dicts(10, 26, 100)

for i in range(len(list_dict)):  # run loop for all elements (dicts) in the list_dict list
    process_each_item_in_dict(list_dict, i, temp_dict, common_dict)

print(common_dict)  # print final result (common_dict)

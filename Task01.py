from random import randrange

# 100 random int values generating
rnd = []  # create empty list
for i in range(100):  # loop: 'when i in range 0-100 do loop body'
    rnd.append(randrange(1000))  # generate and add new random value (from 0 to 1000) into _rnd_ list


# rnd = sorted(rnd) # _rnd_ list sorting

def quick_sort(sequence):  # quick_sort function creation
    length = len(sequence)  # calculate length of sequence
    if length <= 1:  # if length of the sequence less or equal 1 than return sequence (doesn't matter to sort it)
        return sequence
    else:
        pivot = sequence.pop()  # if length of the sequence more than 1 than return the last element of the sequence and then remove it

    items_greater = []  # list for items greater than the value in comparison
    items_lower = []  # list for items less than the value in comparison

    for item in sequence:  # loop for sequence elements
        if item > pivot:  # if item greater than sequence.pop()
            items_greater.append(item)  # then insert it in the items_greater list

        else:  # if item less than sequence.pop()
            items_lower.append(item)  # then insert it in the items_lower list

    return quick_sort(items_lower) + [pivot] + quick_sort(
        items_greater)  # repeat quick_sort for items_lower and items_greater lists and return "items_lower, pivot, items_greater"


# print(quick_sort(rnd))

# list of _chetn_ values
chetn = [i for i in rnd if i % 2 == 0]  # find chetn values in _rnd_ list
print('chetn AVG is: ', sum(chetn) / len(chetn))  # print AVG calculation (sum/cnt)

# list of _nechetn_ values
nechetn = [i for i in rnd if i % 2 != 0]  # find nechetn values in _rnd_ list
# number of elements in the list
print('nechetn AVG is: ', sum(nechetn) / len(nechetn))  # print AVG calculation (sum/cnt)

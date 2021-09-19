from random import randrange

# 100 random int values generating
rnd = []  # create empty list
for i in range(100):  # loop: 'when i in range 0-100 do loop body'
    rnd.append(randrange(1000))  # generate and add new random value (from 0 to 1000) into _rnd_ list
    i + 1  # increase i after each loop body execution


# rnd = sorted(rnd) # _rnd_ list sorting

def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:  # less than = 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:  # greater than pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

# print(quick_sort(rnd))

# list of _chetn_ values
chetn = [i for i in rnd if i % 2 == 0]  # find chetn values in _rnd_ list
print('chetn AVG is: ', sum(chetn) / len(chetn))  # print AVG calculation (sum/cnt)

# list of _nechetn_ values
nechetn = [i for i in rnd if i % 2 != 0]  # find nechetn values in _rnd_ list
# number of elements in the list
print('nechetn AVG is: ', sum(nechetn) / len(nechetn))  # print AVG calculation (sum/cnt)

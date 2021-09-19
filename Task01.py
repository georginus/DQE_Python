from random import randrange

# 100 random int values generating
rnd = []  # create empty list
for i in range(100):  # loop: 'when i in range 0-100 do loop body'
    rnd.append(randrange(1000))  # generate and add new random value (from 0 to 1000) into the rnd list


# rnd = sorted(rnd) # rnd list sorting


def quick_sort(sequence):  # quick_sort function creation
    length = len(sequence)  # calculate length of sequence
    if length <= 1:  # if length of the sequence less or equal 1 than return sequence (doesn't matter to sort it)
        return sequence
    else:
        pivot = sequence.pop()  # if length of the sequence more than 1 than return the last element of the sequence
        # and then remove it

    items_greater = []  # list for items greater than the value in comparison (sequence.pop())
    items_lower = []  # list for items less than the value in comparison (sequence.pop())

    for item in sequence:  # loop for sequence elements
        if item > pivot:  # if item greater than pivot element (sequence.pop())
            items_greater.append(item)  # then insert it in the items_greater list

        else:  # if item less than pivot element (sequence.pop())
            items_lower.append(item)  # then insert it in the items_lower list

    return quick_sort(items_lower) + [pivot] + quick_sort(
        items_greater)  # recursive call quick_sort function for items_lower and items_greater lists and return
    # "items_lower, pivot, items_greater"


rnd = quick_sort(rnd) # call quick_sort for the rnd list
# print(rnd)

# list of even values
even = [i for i in rnd if i % 2 == 0]  # find even values in the rnd list
print('AVG of even numbers is: ', sum(even) / len(even))  # print AVG calculation (sum/cnt)

# list of odd values
odd = [i for i in rnd if i % 2 != 0]  # find odd values in the rnd list
# number of elements in the list
print('AVG of odd numbers is: ', sum(odd) / len(odd))  # print AVG calculation (sum/cnt)

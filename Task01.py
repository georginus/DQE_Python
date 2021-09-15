from random import randrange

# 100 random int values generating
i = 0 # start loop from i
n = 100 # end loop of n
r = 1000 # max random value
rnd = [] # create empty list
for i in range(i, n): # loop: 'when i in range 0-100 do loop body'
    rnd.append(randrange(r)) # generate and add new random value (from 0 to 1000) into _rnd_ list
    i+1 # increase i after each loop body execution
rnd = sorted(rnd) # _rnd_ list sorting

# list of _chetn_ values
chetn = [i for i in rnd if i % 2 == 0] # find chetn values in _rnd_ list
print('chetn AVG is: ', sum(chetn)/len(chetn)) # print AVG calculation (sum/cnt)

# list of _nechetn_ values
nechetn = [i for i in rnd if i % 2 != 0] # find nechetn values in _rnd_ list
# number of elements in the list
print('nechetn AVG is: ', sum(nechetn)/len(nechetn))# print AVG calculation (sum/cnt)


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
chetn_avg = sum(chetn)/len(chetn) # AVG calculation (sum/cnt)
print('chetn AVG is: ', chetn_avg) # print chetn AVG

# list of _nechetn_ values
nechetn = [i for i in rnd if i % 2 != 0] # find nechetn values in _rnd_ list
# number of elements in the list
nechetn_avg = sum(nechetn)/len(nechetn) # AVG calculation (sum/cnt)
print('nechetn AVG is: ', nechetn_avg) # print nechetn AVG

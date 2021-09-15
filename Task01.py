from random import randrange

# 100 random int values generating
i = 0 # start loop from i
n = 100 # end loop of n
r = 1000 # boarding of random values
rnd = []
for i in range(i, n):
    rnd.append(randrange(r))
    i+1


print(rnd)
#
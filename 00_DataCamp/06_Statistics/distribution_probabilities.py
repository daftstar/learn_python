import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

tails = [0]


# to find distribution, create empty list 
# list contains # of tails 
final_tails = []


# in a 100 coin toss
for x in range(1000):
    tails = [0]

    # simulate single game, single game = 10 tosses
    for x in range(10):
        coin = np.random.randint(0,2)
        tails.append(tails[x] + coin)

    # show total number of tails thrown in each game
    print (tails)  

    # append the final tails value in the array
    final_tails.append(tails[-1])

# print (tails)
print ("\n________________\n")
print (final_tails)




# We have the distribution, now show how many times each was counted
# use HISTOGRAM


# initialize histogram
plt.hist(final_tails, bins = 10)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
# show all values of np arrays
# np.set_printoptions(threshold=np.inf)


np.random.seed(123)

# initalize all_walks
all_walks = []


# SIMULATE RANDOM WALK DISTRIBUTION - play game 500 times: 
for i in range(500):
    random_walk = [0]
    for x in range(100):   # play the game (1 game = 100 rolls of dice)
        step = random_walk[-1]
        dice = np.random.randint(1, 7)

        if dice <= 2:
            step = max(0, step - 1)  # cannot go below 0 steps
        elif dice <= 5:
            step += 1
        else:
            step += np.random.randint(1, 7)

        # implement clumsiness model of falling down stairs
        if np.random.rand() <= 0.001:
            step = 0

        # append step to random walk array
        random_walk.append(step)

    # print (random_walk)
    # print ("\n______________\n")
    all_walks.append(random_walk)



# CONVERT all_walks TO NUMPY ARRAY
np_aw = np.array(all_walks)


# PLOT np_aw and how
# the axes are incorrect, we need to transpose
# plt.plot(np_aw)
# plt.show()

# Transpose np_aw to np_aw_t to clean up chart
# every row in np_all_walks represents
# the position after 1 throw for the 10 random walks.

np_aw_t = np.transpose(np_aw)
# print (np_aw)
# print (np_aw_t)


# Initialize and show NON-TRANSPOSED plot
# plt.plot(np_aw)
# plt.show()
# plt.clf()

# Initialize and show TRANSPOSED plot
# plt.plot(np_aw_t)
# plt.show()

# Clear figure
plt.clf()


# ###############################################
# SOLVE:
# What are the odds that you'll reach 60 steps high 
# on the Empire State Building?
# ###############################################

# SELECT ENDPPOINTS FROM ARRAY: np_aw_t
ends = np_aw_t[-1]
print (ends)

# PLOT HISTOGRAM AND DISPLAY
plt.hist(ends)
plt.show()


# ###############################################
# CALCULATE ODDS:
# To calculate the chance that this end point is greater than
# or equal to 60, you can count the number of integers in ends
# that are greater than or equal to 60 and divide that number by 500,
# the total number of simulations.
# ###############################################

total_count = 0
for i in ends:
    if i >= 60:
        total_count +=1

print (total_count)
print (total_count / 500)


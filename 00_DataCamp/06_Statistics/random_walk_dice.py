import numpy as np

# A succession of random steps = random walk
# _____________________________________

# GAME INSTRUCTIONS
#   100 steps available
#   1, 2 = 1 step backwards
#   3, 4, 5 = 1 step forward
#   6 = roll again + n steps forward based on n
#
#   Cannot go below 0
#
#   0.1% chance falling
#    falling = start at very beginning
# Set seed for future random numbers for reproducible results
#
# # SIMULATE RANDOM DICE THROW
# np.random.seed(123)
# print (np.random.randint(1,7))
# print (np.random.randint(1,7))

# _____________________________________

# #############################################
# CREATE RANDOM WALK OF DICE THROWS (100 Throws)
# ############################################

# set random seed for consistency
np.random.seed(123)


# Initialize random walk
random_walk = [0]


# 100 dice throws
for x in range(100):
    # Set step: last element in random_walk
    step = random_walk[-1]

    # roll the dice
    dice = np.random.randint(1, 7)

    # determine next step
    if dice <= 2:
        step = max(0, step - 1)  # cannot go below 0 steps
    elif dice <= 5:
        step += 1
    else:
        step += np.random.randint(1, 7)

    # append step to random walk array
    random_walk.append(step)

print (random_walk)


# #############################################
# VISUALIZE STEPS IN PYPLOT
# ############################################

# initialize pyplot (usually this goes at top of file)
import matplotlib.pyplot as plt

# initialize the plot
plt.plot(random_walk)

# display the plot
plt.show()

import numpy as np

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



# Set seed for future random numbers for reproducible results
np.random.seed(123)

# Initialize step counter
step = 50

# Roll the dice
dice = np.random.randint(1,7)
print (dice)
if dice <= 2:
    step -= 1
elif dice <= 5:
    step += 1
else:
    step += np.random.randint(1,7)  # generate new dice value, add to step count

print (dice)
print (step)
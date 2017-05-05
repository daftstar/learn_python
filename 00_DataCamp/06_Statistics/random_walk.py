import numpy as np

# A succession of random steps = random walk

# BELOW IS NOT A RANDOM WALK AS WE'RE NOT RECORDING THE DIFFERENCES
# set random seed for consistency
np.random.seed(123)

# create a list to capture results
outcomes = []

# create random walk of 10 games of coin-toss
for x in range(10):
    coin = np.random.randint(0, 2)
    # print (coin)
    if coin == 0:
        outcomes.append("heads")
    else:
        outcomes.append("tails")
print (outcomes)


# ___________________________________________________________________
# CREATE RANDOM WALK BY COUNTING TAILS / HEADS

np.random.seed(123)

# initialize tails count to 0
tails = [0]

for x in range(10):
    coin = np.random.randint(0, 2)
    tails.append(tails[x] + coin)

print (tails)

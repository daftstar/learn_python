import numpy as np
# numpy has built-in random number generator



# SIMULATE A COINTOSS
print (np.random.rand())
print (np.random.rand())

# all random below this will be based on seed
np.random.seed(123)
print (np.random.rand())
print (np.random.rand())

# SIMULATE COIN TOSS
np.random.seed(123)
coin = np.random.randint(0, 2)
# because of the seed, the coin will always be 0.
print (coin)

if coin == 0:
    print ("heads")
else:
    print ("tails")


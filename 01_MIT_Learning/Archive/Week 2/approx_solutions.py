# cube = 27
# guess = 0.0

# epsilon = 0.01
# increment = 0.0001

# num_guesses = 0


# while abs(guess ** 3 - cube) >= epsilon:
#     guess += increment
#     num_guesses += 1
# print ('Number of guesses is now at: %s' % num_guesses)



# if abs(guess ** 3 - cube) >= epsilon:
#     print ("Failed on cube rute of %s" % cube)
# else:
#     print ("%s is the closest value to the cube root of: %s" % (guess, cube))

# ##################################
# #### FIX TO STOP INFINITE LOOPS 

# guess = 0
# cube = 27
# increment = 0.01
# epsilon = 0.01

# num_guesses = 0


# while abs(guess ** 3 - cube) >= epsilon and guess <= cube:
#     guess += increment
#     num_guesses += 1
#     print ("Current guess is: %s" % guess)
#     print ("%s cubed is: " % guess, str(guess ** 3)) 
#     # print ("Current count is: %s" % num_guesses)
#     print ("\n#######################\n")

# print ("num_guesses = %s" % num_guesses)

# if abs(guess ** 3 - cube) >= epsilon:
#     print ("Failed on cube root of %s" % cube)
# else:
#     print ("%s is close to the cube root of: %s" % (guess, cube))

# x = 17
# epsilon = 0.01
# step = 0.001
# guess = 0.0
# count = 0

# while guess <= x:
#     if abs(guess**2 -x) < epsilon:
#         break
#     else:
#         guess += step
#         print ("guess is at: %s" % guess)

# if abs(guess ** 2 - x) >= epsilon:
#     print ("failed")
# else:
#     print ("succeeded: %s" % guess)

### ALTERNATE WAY ###
# while abs(guess ** 2-x) >= epsilon:
#     if guess <= x:
#         guess += step
#         count += 1
#     else:
#         break

# if abs(guess ** 2 - x) >= epsilon:
#     print('failed')
# else:
#     print('succeeded: ' + str(guess))

# print ("Total number of guesses = %s" % count)



# ### BISECTIONAL SQRT SEARCH ####


x = 17  # this code cannot use x < 1

high = x
low = 0
ans = (high + low) / 2.0

epsilon = 0.01
num_guesses = 0

while abs(ans ** 2 - x) >= epsilon:
    num_guesses += 1

    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0

print ("\n")
print ("Total Number of Guesses = %s" % num_guesses)
print ("%s is close to the square root of %s" % (ans, x))





# while abs(ans ** 2 - x) >= epsilon:
#     print (" \n\nGUESS # %s" % (num_guesses + 1))
#     print ("---------------------------")
#     print ("  low     = %s" % low)
#     print ("  high    = %s" % high)
#     print ("  new ans = %s" % ans)
#     # print ("\n ######## \n")
#     num_guesses += 1

#     if ans ** 2 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low) / 2.0

# print ("\n")
# print ("Total Number of Guesses = %s" % num_guesses)
# print ("%s is close to the square root of %s" % (ans, x))




# ### BISECTIONAL CUBE ROOT SEARCH ###

# cube = 27

# high = cube
# low = 0
# guess = (high + low) / 2.0

# epsilon = 0.1
# num_guesses = 0


# while abs(guess ** 3 - cube) >= epsilon:
#     print (" \n\nGUESS # %s" % (num_guesses + 1))
#     print ("---------------------------")
#     print ("  low     = %s" % low)
#     print ("  high    = %s" % high)
#     print ("  new guess = %s" % guess)
#     # print ("\n ######## \n")
#     num_guesses += 1

#     if guess ** 3 < cube:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low) / 2.0

# print ("\n")
# print ("Total Number of Guesses = %s" % num_guesses)
# print ("%s is close to the cube root of %s" % (guess, cube))







# Not all objects are accessible everywhere in a script
# Scope - part of the program where an object or name may be accessible

# 3 types of scopes:
# - Global Scope - defined in the main body of a script
# - Local Scope - defined within a function - cannot be access outside of function
# - Built in Scope - built-in (e.g. print())

# for new line 
def new_line():
    print("\n__________________________\n")


# EXAMPLE GLOBAL SCOPE:

new_val = 10

def square(value):
    """ returns the square of a number """
    global new_val
    new_val = new_val ** 2
    return (new_val)

print ("current value of new_val:", new_val)

square(3)
print ("    new value of new_val:", new_val)

new_line()
# ______________________________________________


team = "teen titans"

def change_team():
    """Change the value of the global variable team"""
    # define team as global variable
    global team

    # change value of team name
    team = "justice league"

print ("current value of team:", team)
change_team()
print ("    new value of team:", team)

# ______________________________________________
new_line()




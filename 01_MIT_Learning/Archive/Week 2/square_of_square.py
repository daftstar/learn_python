def square(x):
    """
    x: int or float
    """
    return (x * x)




def fourthPower(x):

    '''
    x: int or float. 
    '''
    forth = square(x) * square(x)
    return forth



# YOU CAN ALSO DO THIS: 
# def fourthPower(x):

#     '''
#     x: int or float. 
#     '''
#     return square(x) * square(x)



print(fourthPower(8.63))

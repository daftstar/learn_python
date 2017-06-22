test = ('I', 'am', 'a', 'test', 'tuple')



# def oddTuples(aTup):
#     '''
#     aTup: a tuple
    
#     returns: tuple, every other element of aTup. 
#     '''
#     odds = ()
#     count = 0

#     for i in aTup:
#         if (count % 2) == 0:
#             odds = odds + (i,)
#         count += 1
#     return (odds)


def oddTuples(aTup):
    return (aTup[::2])

print (oddTuples(test))


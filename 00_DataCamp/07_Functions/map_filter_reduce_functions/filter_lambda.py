# filter() filters out elements from a list that don't satisfy certain criteria

# http://www.python-course.eu/lambda.php

fib = [0,1,1,2,3,5,8,13,21,34,55]
result_filter = filter(lambda x: x % 2 == 0, fib)
print (list(result_filter))

#######

# use filter() call to pass lambda function and list of strings, fellowship
# lambda should check if number of characters in string, member
# is > 6. Assign the resulting filter object to result.


fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']


# ####################################
# TRADITIONAL WAY
# ####################################

def filter_fellowship(member_names):
    result_list = []
    for i in member_names:
        if len(i) > 6:
            result_list.append(i)
    return (result_list)


print (filter_fellowship(fellowship))


#
# ####################################
# LAMBDA FILTER WAY
# ####################################

result = filter(lambda member: len(member) > 6, fellowship)
result_list = (list(result))
print(result_list)


people = 30 
cars = 40
trucks = 15


if cars > people:
    print ("We should take the cars")
elif cars < people:
    print ("We should not take the cars")
else:
    print ("We still don't know")


if trucks > cars: 
    print ("That's too many trucks")
elif trucks < cars:
    print ("Maybe we could take the trucks")
else:
    print ("We still can't decide")


if people > trucks: 
    print ("alright, let's just take the trucks then")
else:
    print ("Fine, let's stay home then")



# Similar to the else, the elif statement is optional. 
# However, unlike else, for which there can be at most one statement, 
# there can be an arbitrary number of elif statements following an if.
# Core Python does not provide switch or case statements as in other languages, 
# but we can use if..elif...statements to simulate switch case as follows −
# elif continues to check other true values. 
# else is the false value command (optional)

print ("\n################################\n")

var = 100
if var == 200:
    print ("1 - got a true expression value")
    print (var)
elif var == 150:
    print ("2 - got a true expression value")
    print (var)
elif var == 100: 
    print ("3 - Got a true expression value")
    print (var)
else:
    print ("4 - Got a false expression value")
    print (var)

print ("Good Bye")

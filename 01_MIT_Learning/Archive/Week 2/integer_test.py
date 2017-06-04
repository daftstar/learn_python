a = int(10.33)
b = a




while type(a) == int:
    print ("a is %s" % type(a))

    a = a + 44.34
    print (a)

    if type(a) != int:
        print ("a is NOT an integer: " + str(type(a)))
        print ("converting to integer now")

    elif type(a) == int:
        print ("a IS an integer: " + type(a))





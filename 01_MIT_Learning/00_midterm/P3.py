def new_line():
    return ("\n__________________________\n")


# 3 - 1
# stuff = ["a", "b", "c"]
# stuff = ("a", "b", "c")
# stuff = [("a", "b", "c")]
# stuff = (["a", "b", "c"], 33, [101, 3939, "jhee"])
# stuff = (["a", "b", "c", "hello"],)
stuff = (["a", "b", "c", "hello"])

# stuff = ["hello"]
# stuff = "hello"


# print (stuff)


for thing in stuff:
    print (thing)
    if thing == "hello":
        print ("Found it")

print (new_line())

# 3 - 2

def Square(x):
    return (square_h(abs(x), abs(x)))

def square_h(a, b):
    if a == 0:
        return 0
    return square_h(a-1, b) + b

# print (square_h(3, 11))
print (Square(10))
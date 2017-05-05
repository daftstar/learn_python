"""
Let's build our own GROCERY STORE
"""

total_inv_value = 0  # this will be used for calculating value of inventory

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}


# for item in prices:
#     print ("%s" % item)
#     print ("price: %s" % prices[item])
#     print ("stock: %s" % stock[item])
#     print ()


# for item in prices:
#     total_inv_value = total_inv_value + (prices[item]) * (stock[item]) 
#     # print ("current total_inv_value is: %d" % total_inv_value)


# print (total_inv_value)


"""
LETS THINK ABOUT THE CUSTOMER
In order for customers to order online, 
we are going to have to make a consumer interface
"""

shopping_list = ["banana", "orange", "apple", "apple", "banana", "pear", "pear"]
# shopping_list = ["apple", "apple"]

# def compute_bill(food):
#     total = 0
#     for item in food:
#         total = total + (prices[item])
#     return (total)

# print (compute_bill(shopping_list))



def compute_bill(food):
    total = 0

    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1

        else:
            total = total

    return (total)

print (compute_bill(shopping_list))









"""
list = {
    "Aardvark": "A star of a popular children's cartoon show.",
    "Baa": "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# LOOPING THROUGH KEYS
for key in list:
    print (key)

print ("")



# FINDING AND PRINTING KEY VALUES
for key in list:
    print (list[key])


Dictionaries have no order in python.
In other words, when you iterate over a dictionary,
    the order that the keys/items are "yielded" is not
    the order that you put them into the dictionary.
    (Try your code on a different version of python
    and you're likely to get differently ordered output).
    If you want a dictionary that is ordered,
    you need a collections.OrderedDict
    which wasn't introduced until python 2.7.
    You can find equivalent recipes on ActiveState
    if you're using an older version of python.
    However, often it's good enough to just sort the
    items (e.g. sorted(mydict.items()).

EDIT as requested, an OrderedDict example:

from collections import OrderedDict
groupL = OrderedDict()  # groupL for Loop
c = 0
for n in range(0,13):
    c += 1
    l = chr(n+97)
    groupL.setdefault(l,c)

print (groupL)






"""







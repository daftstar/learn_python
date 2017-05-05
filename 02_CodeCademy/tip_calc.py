"""
WITHOUT FUNCTION 
""" 

# meal = 44.50
# tax = 0.0675
# tip = 0.15

# meal = meal + meal * tax
# total = meal + (meal * tip)


# print("$%.2f" % total)  #.2f signals a 2 decimal float. 




"""
WITH FUNCTIONS
"""


def tax(bill):
    # Adds 8% tax to bill
    bill *= 1.08
    print ("With tax, your bill is $ %.2f" % bill)
    return bill


def tip(bill):
    print ("before tip, your bill is: %.2f" % bill)
    # Adds 15% to bill + tax
    bill *= 1.15
    print ("With tip, your total is now: $ %.2f" % bill)
    return bill


meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

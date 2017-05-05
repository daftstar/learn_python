# def answer():
#     return 42


# print (answer())


# def square(n):
#     """ Returns the square of a number """
#     squared = n ** 2
#     print ("%d squared is %d." % (n, squared))
#     return squared

# print (square(3))


# def power(base, exponent):
#     result = base ** exponent
#     return ("%d to the power %d is %d." % (base, exponent, result))


# print (power(37,4))






"""
OR YOU CAN DO IT THIS WAY
"""

# def power(base, exponent):
#     result = base ** exponent
#     print ("%d to the power %d is %d." % (base, exponent, result))


# power(7,2)


# def is_numeric(num):
#     return type(num) == int or type(num) == float


# print (is_numeric(99/33.2))
# max (2, 4, 6)
# min (2, 3, 99)


# def distance_from_zero(num):
#     if type(num) == int or type(num) == float:
#         return abs(num)
#     else:
#         return ("Nope")


# print (distance_from_zero(22))


"""
    LETS TAKE A VACATION
"""


car_rental_rate = 40


def hotel_cost(nights):
    cost = 140
    return cost * nights


def plane_ride_cost(city):
    if city == "Charlotte":
        return 183

    elif city == "Tampa":
        return 220

    elif city == "Pittsburgh":
        return 222

    elif city == "Los Angeles":
        return 475

    else:
        return 1000


def rental_car_cost(days):
    if days >= 7:
        car_cost = (days * car_rental_rate) - 50
        return car_cost

    elif days >= 3 and days < 7:
        car_cost = (days * car_rental_rate) - 20
        return car_cost

    else:
        car_cost = (days * car_rental_rate)
        return car_cost


def trip_cost(city, days, spending_money):
    total_cost = hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money
    return total_cost

# print (hotel_cost(4))
# print (plane_ride_cost("Pittsburgh"))
# print (rental_car_cost(10))
print (trip_cost ("Charlotte", 10, 100))

print (1400 + 183 + 350 + 100)






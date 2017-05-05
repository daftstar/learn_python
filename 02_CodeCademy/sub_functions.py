# def one_good_turn(n):
#     return n + 1


# def deserves_another(n):
#     return one_good_turn(n) + 2


# print (one_good_turn(2))
# print (deserves_another(3))


# Sub Function Cubes
# def cube(number):
#     cubed = number ** 3
#     return (cubed)


# def by_three(number):
#     if number % 3 == 0:
#         return cube(number)
#     else:
#         return False


# print (by_three(2))


def shut_down(s):
    if s == "yes":
        return ("Shutting down")

    elif s == "no":
        return ("Shutdown aborted")

    else:
        return ("Sorry")

print(shut_down("no"))

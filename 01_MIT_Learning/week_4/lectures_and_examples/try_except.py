# # ###########################################
# # REPLACING SYSTEM ERROR MESSAGES: GENERAL
# # ###########################################
# try:
#     a = 45
#     # b = 16
#     # b = 0
#     b = 99
#     # b = ddfs         # change this value to test
#     print (a/b)
#     print ("Okay")
# except:
#     # if an error presents itself, goes to this message
#     print ("HEY, there's a bug in a or b inputs")

# print ("outside of function")

# print ("\n________________________________________________\n")

# # ###########################################
# # REPLACING SYSTEM ERROR MESSAGES: SPECIFIC
# # ###########################################

# try:
#     a = 45
#     # b = 16
#     b = int("sjdfj")
#     # b = 0
#     # b = sdfs
#     # b = "sdfjks"
#     print ("a / b =", a / b)
#     print ("a + b =", a + b)
# except ValueError:
#     print ("Could not convert to a number")
# except ZeroDivisionError:
#     print ("Can't divide by zero")
# except:
#     print ("something went seriously wrong. shit.")

# print ("\n________________________________________________\n")

# # ###########################################
# # REPLACING SYSTEM ERROR MESSAGES: KEEP GOING
# # ###########################################
# # else
# #
# # finally
# #   - always executed


# while True:
#     try:
#         # n = 33
#         # n = 0
#         n = sdfd
#         # n = "w23432"
#         # n = "33"
#         # n = int("33")
#         n = int(n)
#         break
#     except ValueError:
#         print ("ERROR: Input not an integer, try again")
#         break
#     except NameError:
#         print ("ERROR: variable has not been defined")
#         break

# print ("\n________________________________________________\n")


# data = []
# file_name = "something.txt"

# try:
#     fh = open(file_name, 'r')
# except IOError:
#     print ("ERROR: Cannot open", file_name, "\n\n")
# else:
#     for new in fh:
#         if new != "\n":
#             addIt = new[:-1].split(',')  # remove trailing \n
#             data.append(addIt)
# finally:
#     fh.close()  # close file even if fail

# print (data)


# print ("\n________________________________________________\n")


# def fancy_divide(numbers, index):
#     try:
#         denom = numbers[index]
#         for i in range(len(numbers)):
#             numbers[i] /= denom
#     except IndexError:
#         print("-1")
#     else:
#         print("1")
#     finally:
#         print("0")

# print (fancy_divide([0, 2, 4], 1))      # WORKS
# print()
# print (fancy_divide([0, 2, 4], 4))      # -1 error case
# print()
# # print (fancy_divide([0, 2, 4], 0))      # ZeroDivisionError


# def fancy_divide(numbers, index):
#     try:
#         denom = numbers[index]
#         for i in range(len(numbers)):
#             numbers[i] /= denom
#     except IndexError:
#         fancy_divide(numbers, len(numbers) - 1)
#     except ZeroDivisionError:
#         print("-2")
#     else:
#         print("1")
#     finally:
#         print("0")

# print (fancy_divide([0, 2, 4], 0))
# print ()
# print (fancy_divide([0, 2, 4], 1))
# print ()
# print (fancy_divide([0, 2, 4], 4))
# print ()
# print (fancy_divide([0, 2, 4], 0))


def fancy_divide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")

print (fancy_divide([0, 2, 4], 1))
print ()
print (fancy_divide([0, 2, 4], 4))
print ()
print (fancy_divide([0, 2, 4], 0))
print ()


# ####################################
def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)

print (fancy_divide([0, 2, 4], 0))
print ()

# #####################################

def fancy_divide(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception as ex:
        print(ex)

print (fancy_divide([0, 2, 4], 0))

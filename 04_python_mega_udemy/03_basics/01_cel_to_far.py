# function that converts Celsius to Farenheit and vice versa


def convert_c_to_f(celsius):
    far = (celsius * (9/5)) + 32
    return far


def convert_f_to_c(farenheit):
    cel = (farenheit - 32) / (9/5)
    return cel


print (convert_c_to_f(100))
print (convert_f_to_c(212))
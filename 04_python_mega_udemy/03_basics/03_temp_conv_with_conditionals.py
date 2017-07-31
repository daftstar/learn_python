# function that converts Celsius to Farenheit and vice versa


def convert_c_to_f(celsius):
    """celsius is a number (int or float)
    outputs farenheit representation of celsius input"""
    if celsius < -273.15:
        return ("error, no temperature exists below this point")
    else:
        far = (celsius * (9/5)) + 32
        return far


def convert_f_to_c(farenheit):
    cel = (farenheit - 32) / (9/5)
    return cel


# print (convert_c_to_f(-299))
# print (convert_f_to_c(212))


temperatures = [10, -20, -289, 100]

for celsius in temperatures:
    print (convert_c_to_f(celsius))

# function that converts Celsius to Farenheit and vice versa

file = open("temperatures.txt", "a")


def convert_c_to_f(celsius):
    """celsius is a number (int or float)
    outputs farenheit representation of celsius input"""

    if celsius < -273.15:
        return ("error, no temperature exists below this point")
    else:
        far = ((celsius * (9/5)) + 32)
        file.write("celsius:" + str(celsius) + "= " + str(far) + "\n")
        return far


temperatures = [i for i in range(-300, 200)]


for celsius in temperatures:
    print(convert_c_to_f(celsius))

# https://docs.python.org/3/library/datetime.html
import datetime

now = (datetime.datetime.now())

# http://strftime.org
pleasant_time = now.strftime("%a %b %y (%H-%M-%S)")
filename = pleasant_time

def create_file():
    """This function creates an empty file"""
    with open(str(filename)+".txt", "w") as file:
    # with open(str(filename), "w") as file:    # no file extension

        file.write("Hello World!")


create_file()
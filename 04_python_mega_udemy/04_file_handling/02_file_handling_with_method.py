with open("a_new_file", "a+") as file:
    file.seek(0)    # pointer at first line
    content = file.read()
    # do something
    # do somethinng
    # file automatically closed once outside of indent

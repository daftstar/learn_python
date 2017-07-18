class A(object):
    def __init__(self):
        self.a = 1

    def x(self):
        print("A.x")

    def y(self):
        print ("A.y")

    def z(self):
        print ("A.z")


class B(A):     # child of A class
    def __init__(self):
        A.__init__(self)    # call on A __init__ function
        self.a = 2
        self.b = 3

    def y(self):
        print("B.y")

    def z(self):
        print ("B.z")


class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5

    def y(self):
        print ("C.y")

    def z(self):
        print ("C.z")


class D(C, B):  # first C, then B - B can overwrite C
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6

    def z(self):
        print ("D.z")


obj = D()
print (obj.a)   # 2
print (obj.b)   # 3
print (obj.c)   # 5
print (obj.d)   # 6
print()
obj.x()         # A.x       Exists only within Class A
obj.y()         # C.x       Exists only in Class C, B, A
obj.z()         # D.z       Exists in Class D






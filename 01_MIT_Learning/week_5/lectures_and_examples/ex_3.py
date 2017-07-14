class Weird(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return x

    def getY(self):
        return y


class Wild(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

X = 7
Y = 8

w1 = Weird(X, Y)
# print(w1.getX())      # error
# print(w1.getY())      # error


w2 = Wild(X, Y)
print (w2.getX())
print (w2.getY())


w3 = Wild(17, 18)
print (w3.getX())


w4 = Wild(X, 18)
print (w4.getX())

X = w4.getX() + w3.getX() + w2.getX()
print(X)

print(w4.getX())


Y = w4.getY() + w3.getY()       # 18 + 18
Y = Y + w2.getY()               # 36 + 8
print(Y)                        # 44
        


print(w2.getY())

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x-other.x) ** 2
        y_diff_sq = (self.x-other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

c = Coordinate(3, 4)
origin = Coordinate(0, 0)

print (c)                   # <__main__.Coordinate object at 0x100734550>

print (c.x)                 # 3
print (origin.x)            # 0

print (c.distance(origin))  # 4.242640687119285
print (Coordinate.distance(c, origin))
class Clock(object):
    def __init__(self, time):
        self.time = time

    def print_time(self):
        time = '6:30'           # time isn't doing anything here.
        print (self.time)


# clock = Clock("5:30")
# # print (clock)
# clock.print_time()              # 5:30


# with no positional arguments
class Clock(object):
    def __init__(self, time):
        self.time = time

    def print_time(self, time):
        print (time)


# clock = Clock('5:30')
# clock.print_time('10:30')       # 10:30


class Clock(object):
    def __init__(self, time):
        self.time = time

    def print_time(self):
        print (self.time)


boston_clock = Clock('5:30')
paris_clock = boston_clock      # this makes paris & boston identical

paris_clock.time = '10:30'
boston_clock.time = '32323'
boston_clock.print_time()
paris_clock.print_time()

print (boston_clock == paris_clock)




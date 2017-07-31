import datetime

# dependent on computer local time


# then = (datetime.datetime(2016, 5, 14, 11, 0, 0, 0))
then = (datetime.datetime(2016, 11, 2))

now = datetime.datetime.now()

delta = (now - then)
print (delta)
print (delta.days)
# print (delta.hours)
print (delta.total_seconds)
print (delta.seconds)
# any funciton with a yield statement is a generator
# generators have built-in next methonds


def genTest():
    yield 1
    yield 2


print (genTest())

foo = genTest()
print(foo.__next__())     # 1
print(foo.__next__())     # 2
# print(foo.__next__())   # StopIteration exception
print()


for n in genTest():
    print (n)

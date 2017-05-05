
# my_list = []
# for i in range(1, 11):
#     my_list.append(i ** 2)

# SIMPLIFIED COLLECTION STATEMENT: 
my_list = [i **2 for i in range(1, 11)]

print (my_list)

f = open("outout.txt", "w")

for i in my_list:
    f.write(str(i) + "\n")

f.close()
print (f)
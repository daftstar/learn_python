num = 0

while num < 10:
    num += 2
    print (num)

print ("Goodbye!")
print ("\n######\n")

### OR ###

num = 2
while num <= 10:
    print(num)
    num += 2
print ("Goodbye")

print ("\n######\n")

### OR ###
num = 0
while True:
    num += 2
    print (num)
    if num >= 10:
        print ("Goodbye!")
        break

### OR ### 

num = 1
while num <= 10:
    if num % 2 == 0:
        print (num)
        num +=1
print ("Goodbye")

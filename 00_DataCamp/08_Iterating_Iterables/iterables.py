def newline():
    print ("\n______________________________\n")


word = 'Data'
it = iter(word)
print (next(it))
print (next(it))
print (next(it))
print (next(it))
newline()
# -----------------------------------------------------


word2 = "this is everything"
iter_word2 = iter(word2)
print (*iter_word2)

# print (next(iter_word2))  > nothing left to iterate
newline()
# -----------------------------------------------------


# dictionaries and lists are iteratbles.
members = {'me': 'Nik', 'you': 'some person', 'them': 'those people', 'us': 'literally everyone'}

for key, value in members.items():
    print (key, value)


# Iterating over file connections
file = open('file.txt')
file_it = iter(file)
print (next(file_it))
print (next(file_it))
print (next(file_it))
print (next(file_it))
print (next(file_it))
newline()


file = open('file.txt')
file_it = iter(file)
print (*file_it)
newline()
# -----------------------------------------------------


flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

superseed = iter(flash)
print (next(superseed))
print (next(superseed))
print (next(superseed))
print (next(superseed))
newline()
# -----------------------------------------------------

# ############################################
# Iterating through ranges
# ############################################

small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

# Loop over range(3) and print the values
for i in range(3):
    print (i)

# Create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100))

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print (*googol)




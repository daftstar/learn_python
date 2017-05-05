movies = {
    "Monty Python and the Holy Grail": "Great",
    "Monty Python's Life of Brian": "Good",
    "Monty Python's Meaning of Life": "Okay"
}

to print all items in dictionary
for key in movies.items():
    print (key)

to print each key and value in dictionary
for key in movies:
    print (key, movies[key])


print (movies.items())
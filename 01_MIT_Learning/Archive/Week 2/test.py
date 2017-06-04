s, l, g, h = 0, 0, 50, 100

# s = ans
# l = low
# h = high
# g = (low + high) / 2.0


print("Please think of a number between 0 and 100!")
while s != 'c':
    print("Is your secret number",g, "?")
    s = (input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
    if s == 'h':
        h = g
        g = (g + l) // 2
    elif s =='l':
        l = g
        g = (g + h) // 2
    elif s != 'c':
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was:", g)
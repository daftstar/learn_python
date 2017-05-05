from random import randint  # imports randomize features

board = []

"""
STEP 1: 
Create a 5 x 5 grid initialized to all 'O's and store it in board.
"""

for i in range(0, 5):
    board.append(["O"] * 5)


"""
CUSTOM PRINT STATEMENT
Print the board so it's easier to visualize
"""


def print_board(board):
    for row in board:
        # print (row)
        # print (" ---- ".join(row))
        print (" ".join(row))  # this removes all the erroneous characters


print (print_board(board))

# print ("the board currently has: %s rows" % str(len(board)))

"""
RANDOM INTEGER USAGE - 
requires "from random import randint"

# coin = randint(0, 100)
# print (coin)


STEP 2: CREATE HIDDEN SPOT
"""

def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


"""
STEP 3: CREATE USERS GUESSES
"""

# guess_row = int(raw_input("Guess Row: "))
# guess_col = int(raw_input("Guess Col"))

# guess_row = 3
# guess_col = 4

"""
STEP 4: DEBUGGING
"""
print (ship_row)
print (ship_col)



# if guess_row == ship_row and guess_col == ship_col:
#     print ("Congratulations! You sank my battleship!")


"""
STEP 5: ERROR HANDLING
"""

# if guess_row == ship_row and guess_col == ship_col:
#     print ("Congratulations! You sank my battleship!")
# else:
#     print ("You missed my battleship!")
#     board[guess_col] = "X" 
#     board[guess_row] = 'X'
#     print (print_board(board))


"""
ACCOUNTING FOR COMPLETE MISS SITUATIONS
"""

# if guess_row not in range(5) or guess_col not in range (5):
#     print ("Oops, that's not even in the ocean.")
# elif guess_row == ship_row and guess_col == ship_col:
#     print ("Congratulations! You sank my battleship!")
# else:
#     print ("You missed my battleship!")
#     board[guess_col] = "X" 
#     board[guess_row] = 'X'
#     print (print_board(board))


"""
ACCOUNTING FOR PREVIOUSLY GUESSES SPOTS
"""
for turn in range(4):
    print ("Turn", turn + 1)

    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sank my battleship!")
        break

    elif (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        print ("Oops, that's not even in the ocean.")

    elif board[guess_row][guess_col] == "X":
        print ("You guessed that one already.")

    else:
        print ("You missed my battleship!")
        board[guess_row][guess_col] = 'X'

        if turn >= 3:
            print ("Game Over. Took too many turns.")
            break


    print (print_board(board))









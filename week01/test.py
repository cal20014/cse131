import json

# The characters used in the Tic-Tac-Too board.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return data['board']
    except FileNotFoundError:
        return blank_board['board']

def save_board(filename, board):
    '''Save the current game to a file.'''
    with open(filename, 'w') as f:
        json.dump({"board": board}, f)

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("---+---+---")

def is_x_turn(board):
    '''Determine whose turn it is.'''
    return board.count(X) <= board.count(O)

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    while not game_done(board, True):
        display_board(board)
        if is_x_turn(board):
            player = X
        else:
            player = O
        move = input(f"It's {player}'s turn. Enter a position (1-9) or 'q' to quit: ")
        if move == 'q':
            save_board('game.json', board)
            return False
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move)-1] == BLANK:
            board[int(move)-1] = player
        else:
            print("Invalid move. Try again.")
    return True

def game_done(board, message=False):
    '''Determine if the game is finished.'''
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True

    return False

# User instructions
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")

filename = 'game.json'
board = read_board(filename)

if play_game(board):
    try:
        import os
        os.remove(filename)
    except FileNotFoundError:
        pass

# Display a message to the user after the game has concluded
print("\nGame Over!")

# Ask the user if they want to play again
while True:
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        board = blank_board['board']
        play_game(board)
    elif play_again == 'no':
        print("Thank you for playing! Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


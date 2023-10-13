# 1. Name:
#      Grant Call
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      The Hardest part of this lab was figuring out the code given to me.
#      I usually find it easier to work with my code from scratch.
#      This was good practice looking at someone else's code and working with it.
# 5. How long did it take for you to complete the assignment?
#      6 hours

import json

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '
turn = 0

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    try:
        with open(filename, "r") as file_handle:
            json_data = file_handle.read()
            dictionary_data = json.loads(json_data)
            return dictionary_data

    except:
        print(f"There was an error. The file: {filename} could not be found")
    return blank_board['board']

def save_board(filename, board):
    '''Save the current game to a file.'''
    # Put file writing code here.
    try:
        with open(filename, "w") as file_handle:
            json_data = json.dumps(board)
            file_handle.write(json_data)
    except:
        print(f"There was an error. The file: {filename} could not be found")


def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def is_x_turn(board):
    '''Determine whose turn it is.'''
    # Put code here determining if it is X's turn.
    return board.count(X) <= board.count(O)

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    # Put game play code here. Return False when the user has indicated they are done.
    
    while True:
        display_board(board)

        # Determine whose turn it is
        if is_x_turn(board):
            current_turn = X
        else:
            current_turn = O

        # Get player input with prompt and remove any whitespace that might cause and error.
        player_choice = input(f"{current_turn}> ").strip()

        # Quit logic
        if player_choice.lower() == "q":
            save_board("game_board.json", board)
            print("The Game was saved!")
            print("run the game again to start where you left off")
            return False

        try:
            if int(player_choice) >= 0 and int(player_choice) <= 9:
                player_choice = int(player_choice)

                # checks the spot if it has been taken.
                if board[player_choice - 1] == BLANK:
                    board[player_choice - 1] = current_turn

                    # check if the game is finished, display finished board and the winning message, and reset the board.
                    if game_done(board, message=False) == True:
                        display_board(board)
                        game_done(board, message=True)
                        save_board("game_board.json", blank_board["board"])
                        return True
                    
                else:
                    print("That spot has already been taken. Choose a different spot.")
        except:
            print(f"Invalid input: {player_choice} is not correct.")
            print("please choose a number between 1-9")


def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print(f"The game was won by {board[row * 3]}!")
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print(f"The game was won by {board[col]}!")
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print(f"The game was won by {board[4]}!")
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

def info_display_message():
    # These user-instructions are provided and do not need to be changed.
    print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
    print("where the following numbers correspond to the locations on the grid:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")
    print("The current board is:")


def main():
    """
    Displays start message
    Reads in a the previous game
    Begins the game
    """
    info_display_message()
    board = read_board("game_board.json")
    play_game(board)

if __name__ == "__main__":
    main()
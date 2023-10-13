# https://www.geeksforgeeks.org/json-dumps-in-python/

# 1. Name:
#      Grant Call
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

import json

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def get_file():
    """
    Prompts the user to enter the name of the file.
    Returns:
        str: The name of the file entered by the user.
    """
    filename = input("What is the name of the file? ")
    return filename

def read_board(filename):
    """
    Reads a JSON file and returns a dictionary representing a tic-tac-toe board.
    
    Parameters:
    - filename (str): The name of the JSON file to read.
    
    Returns:
    - dict: A dictionary representing the tic-tac-toe board. 
            If the JSON file does not have the expected structure, 
            it will return a blank board.
            
    Example:
    Expected JSON structure:
    {
        "board": [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    }
    
    Usage:
    board = read_json_to_dict("board.json")
    """
    with open(filename, 'r') as file:
        board = json.load(file)
    
    # Verify that the JSON structure is correct
    if "board" in board and len(board["board"]) == 9:
        return board
    else:
        # Return a blank board if the structure is not correct
        return {
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK
            ]
        }



def save_board(filename, board):
    """
    Saves a dictionary representing a tic-tac-toe board to a JSON file.
    
    Parameters:
    - data (dict): The dictionary representing the tic-tac-toe board.
    - filename (str): The name of the JSON file to save to.
    
    Returns:
    - None: The function writes to a file and doesn't return anything.
    
    Usage:
    board_data = {
        "board": [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    }
    save_dict_to_json(board_data, "board.json")
    """
    
    with open(filename, 'w') as file:
        json.dump(board, file, indent=4)

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    # Put display code here.

def is_x_turn(board):
    '''Determine whose turn it is.'''
    # Put code here determining if it is X's turn.
    return True

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    # Put game play code here. Return False when the user has indicated they are done.
    return False

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
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
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

# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")

# The file read code, game loop code, and file close code goes here.

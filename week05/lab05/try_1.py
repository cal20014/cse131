import os.path
import json

def get_filename():
    """Prompt user for a filename and return it."""
    while True:
        filename = input("Enter a filename: ")
        if os.path.isfile(filename):
            return filename
        else:
            print("File does not exist.") 
   
def read_board(filename):
    """
    Read a Sudoku board from the given file; return a list of lists of ints.

    Parameters:
        filename (str): The path to the JSON file.
        
    Returns:
        dictionary: The board from the JSON file.
    """
    try:
        with open(filename, 'r') as file:
            json_data = json.load(file)
            board = json_data['board']
        return board
    except FileNotFoundError:
        print(f"No such file or directory: '{filename}'")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file: '{filename}'")

def display_board(board):
    print("A B C D E F G H I")
    for row in range(0, 8):
        if row == 3 or row == 6:
            print("--+--+--+")
        for col in range(0, 8):
            separator = "  |  |  \n"
            print(board[row][col], end="")
            print(separator[col], end="")
    

def get_coordinates(board):
    return row, col

def validate_coordinates(board, row, col):
    pass

def save_game(board, filename):
    pass

def get_input_value(board, row, col):
    return value

def validate_input_value(value):
    pass

def display_hint_options(board, row, col):
    pass

def update_board(board, row, col, value):
    return updated_board


def play_game(board):
    """
    Play a game of Sudoku interactively with the user.

    Parameters:
        board (list): The Sudoku board.
    """

        

def main():
    filename = get_filename()
    board = read_board(filename)

    play_game(board)
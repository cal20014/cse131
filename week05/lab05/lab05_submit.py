# 1. Name:
#      Grant Call
# 2. Assignment Name:
#      Lab 05 : Sudoku Draft
# 3. Assignment Description:
#      This program will allow the user to play a game of Sudoku.
#      The program will prompt the user for a filename, read the file,
#      and display the board. The program will then prompt the user
#      for a coordinate to edit, validate the input, and prompt the user
#      for a value to enter in the specified coordinate.
#      The program will validate the input and update the board
#      with the new value. The program will continue to prompt the user
#      for coordinates and values until the user enters 'Q' to save and quit.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was figuring out how to Display the board,
#      parse the coordiantes, and validate the coordinates.
#      I spent a lot of time reconfiguring my code to get it to work.
#     I also had a hard time figuring out how to exit the game.
# 5. How long did it take for you to complete the assignment?
#      15 hours

# Citation:
# Brother Godderidge - helped me with debugging my code
# and fixing my get_coordinates function.
# He also heled with the overall design of the program.
# He also helped me with the parse_coordinates function.
# chatgpt - Helped me with documenting my functions
# and generating doc string template.

import os.path
import json

def get_filename():
    """
    Prompts user for a filename and return it.
    
    The function repeatedly prompts the user for a filename until a file 
    with that name is found in the system. 
    
    Returns:
        str: A string containing the filename provided by the user.
    """
    while True:
        filename = input("Enter a filename: ")
        if os.path.isfile(filename):
            return filename
        else:
            print("File does not exist.") 
   
def read_board(filename):
    """
    Reads a Sudoku board from the specified file and return a board.
    
    The function attempts to read a JSON file and extract the Sudoku board
    from it. Errors are handled for file not found and JSON decoding issues.
    
    Parameters:
        filename (str): The path to the JSON file.
        
    Returns:
        list of lists of integers: The Sudoku board extracted from the JSON file.
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
    """
    Displays the Sudoku board in a user-friendly format.
    
    Parameters:
        board (list of lists of integers): The Sudoku board to display.
    """
    # Display the column headers
    print("   A B C D E F G H I")
    
    for row in range(9):
        # Adding a separator line after every 3 rows
        if row == 3 or row == 6:
            print("   -----+-----+-----")
        
        # Displaying the row number (adding 1 to start from 1 instead of 0)
        print(f"{row + 1}  ", end="")

        for column in range(9):
            # Deciding which separator to use based on the column number
            separator = "|" if column == 2 or column == 5 else " "
            # Displaying the board value or a space if the value is 0
            print(f"{board[row][column] or ' '}{separator}", end="")
        print()  # Moving to the next line after printing each row

    

def get_coordinates(board, filename):
    """
    Prompts the user to input coordinates for editing a Sudoku board or to quit the game.
    
    This function repeatedly asks the user to specify a grid coordinate on the Sudoku 
    board for editing, or to enter 'Q' to save the current state of the board and quit 
    the game. Coordinates should be specified in the format [Letter][Number] (e.g., A1, B2, etc.), 
    where the letter represents the row (A-I) and the number represents the column (1-9).
    The function validates the user's input and provides feedback on any invalid entries.
    
    Parameters:
        board (list of lists of integers): The current state of the Sudoku board, represented as a 9x9 nested list.
        filename (str): The name of the file where the board should be saved if the user chooses to quit.
    
    Returns:
        tuple: A 4-tuple containing the following elements:
            - row (int): The parsed row index derived from the entered coordinates.
            - column (int): The parsed column index derived from the entered coordinates.
            - done (bool): A flag indicating whether the user has chosen to quit.
            - coordinates (str): The raw coordinate string entered by the user.
    """
    valid = False
    while not valid:
        row = 0
        column = 0
        done = False
        coordinates = input("Specify a coordinate to edit or 'Q' to save and quit: e.g. A1, C7, I9, Q: ")
        if len(coordinates) == 2:
            valid_coordinates = validate_coordinates(coordinates[1], coordinates[0])
            row, column = parse_coordinates(coordinates)
            if valid_coordinates == True:
                valid = True
            else:
                print("Invalid input: Coordinates must be between A1 and I9 or 'Q' to save and quit")
        elif coordinates.lower() == 'q':
            done = handle_input_value(board, filename, row, column, coordinates, coordinates)
            valid = True
        else:
            print("Invalid input: Coordinates must be between A1 and I9 or 'Q' to save and quit")
    return row, column, done, coordinates


def parse_coordinates(coordinates):
    row = 0
    column = 0
    letter = coordinates[0].upper()
    if "A" <= letter <= "I":
        column = ord(letter) - ord("A")
    number = int(coordinates[1])
    if 1 <= number <= 9:
        row = int(number) - 1
    return row, column

def validate_coordinates(row, column):
    """
    Validate whether the given Sudoku coordinates are within acceptable bounds.
    
    Parameters:
        row (int): The row coordinate to validate.
        column (str): The column coordinate to validate.
        
    Returns:
        bool: True if coordinates are valid, False otherwise.
    """
    row = int(row)
    if row >= 1 or row <= 9 and column >= "A" or column <= "I":
        return True
    else:
        return False
    

def save_game(board, current_filename):
    """
    Prompt the user to save the current game state to a file.
    
    The function allows the user to save to a new file or override
    the current file. It will repeatedly ask for input until a valid
    response is provided.
    
    Parameters:
        board (list of lists of int): The current state of the Sudoku board.
        current_filename (str): The filename of the current game state.
    """
    saved = False
    while not saved:
        save_message = input("Save to a new file or override the current file? (n/c): ")
        if save_message.lower() == "n":
            new_filename = input("Enter a new filename: ")
            with open(new_filename, 'w') as file:
                json.dump({"board": board}, file)
                saved = True
        elif save_message.lower() == "c":
            with open(current_filename, 'w') as file:
                json.dump({"board": board}, file)
                saved = True
        else:
            print("Invalid input: Enter 'n' or 'c'")

def get_input_value():
    """
    Prompts the user to input a value for editing a Sudoku cell, requesting a hint, or quitting the game.

    The function continuously prompts the user to enter a value until a valid input is provided. 
    The valid inputs are:
        - A number between 1 and 9 (inclusive) for filling a Sudoku cell.
        - 's' to request a hint for possible numbers that could be filled into a selected Sudoku cell.
        - 'q' to save the current state of the Sudoku board and quit the game.

    The function utilizes the 'validate_input_value' function to check the validity of the user input 
    and provides feedback in case of invalid entries. It returns the valid input value once it is received.

    Returns:
        str: A string representing the validated user input, which could be a digit ('1'-'9'), 's', or 'q'.
    """
    valid = False
    while not valid:
        value = input("Enter a number between 1 and 9 or enter 's' for a hint or 'q' to save and quit:")
        if validate_input_value(value):
            valid = True
            return value
        else:
            print("Invalid input: Enter a number between 1 and 9, 's' for a hint, or 'q' to quit and save")

def handle_input_value(board, filename, row, column, coordinates, value):
    """
    Handle the input value provided by the user.
    
    If the user enters 's', display possible values for the given cell.
    If 'q', save the current game state and quit. Otherwise, update the
    board with the given value.
    
    Parameters:
        board (list of lists of int): The current state of the Sudoku board.
        filename (str): The filename of the current game state.
        row (int): The row coordinate of the cell to edit.
        column (str): The column coordinate of the cell to edit.
        value (str): The value provided by the user.
    """
    if value.lower() == "s":
        display_hint_options(board, row, column, coordinates, value)
    elif value.lower() == "q":
        save_game(board, filename)
        return True
    else:
        update_board(board, row, column, value)
    return False

def validate_input_value(value):
    """
    Validate whether the provided input value is within acceptable bounds or commands.
    
    Parameters:
        value (str): The value provided by the user.
        
    Returns:
        bool: True if the input value is valid, False otherwise.
    """
    try:
        # Check if the value is an integer and within [1, 9]
        if 1 <= int(value) <= 9:
            return True
    except ValueError:
        # Check if the value is 's' or 'q'
        if value.lower() == "s" or value.lower() == "q":
            return True
    # If neither condition is met, return False
    return False


def display_hint_options(board, row, column, coordinates, value):
    """
    Display possible valid entries for the specified Sudoku cell.
    
    Parameters:
        board (list of lists of int): The current state of the Sudoku board.
        row (int): The row coordinate of the cell.
        column (str): The column coordinate of the cell.
        value (str): The value to validate as a hint.
    """
    hint_options = []

    print(f"Hint options for {coordinates}: {hint_options}")

def update_board(board, row, column, value):
    """
    Update the specified cell in the Sudoku board with the provided value.
    
    Parameters:
        board (list of lists of int): The current state of the Sudoku board.
        row (int): The row coordinate of the cell to edit.
        column (str): The column coordinate of the cell to edit.
        value (str): The value to set in the specified cell.
        
    Returns:
        list of lists of int: The updated Sudoku board.
    """
    board[row][column] = value
    update_board = board

    return update_board

def play_game(board, filename):
    """
    Play a game of Sudoku interactively with the user.
    
    Parameters:
        board (list of lists of integers): The Sudoku board.
        filename (str): The filename of the current game state.
    """
    done = False
    while not done:
        display_board(board)
        row, column, done, coordinates = get_coordinates(board, filename)

        if done == False:
            value = get_input_value()
            done = handle_input_value(board, filename, row, column, coordinates, value)

    print("Thanks for playing!")

def main():
    """
    The main function.
    This function runs get_filename, read_board, and play_game.
    """
    filename = get_filename()
    board = read_board(filename)
    play_game(board, filename)

if __name__ == "__main__":
    main()
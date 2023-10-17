import os.path
import json

DEBUG = True
TEST = True

def get_filename():
    """
    Prompt user for a filename and return it.
    
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
    Read a Sudoku board from the specified file and return a board.
    
    The function attempts to read a JSON file and extract the Sudoku board
    from it. Errors are handled for file not found and JSON decoding issues.
    
    Parameters:
        filename (str): The path to the JSON file.
        
    Returns:
        list of lists of int: The Sudoku board extracted from the JSON file.
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
    Display the Sudoku board in a user-friendly format.
    
    Parameters:
        board (list of lists of int): The Sudoku board to display.
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
            # Displaying the board value or a space if it's None/0
            print(f"{board[row][column] or ' '}{separator}", end="")
        print()  # Moving to the next line after printing each row

    

def get_coordinates():
    """
    Prompt the user for Sudoku coordinates and return them as a tuple.
    
    The function ensures that the provided coordinates are valid by 
    using validate_coordinates function. It will repeatedly ask for 
    input until valid coordinates are provided.
    
    Returns:
        tuple of (int, str): A tuple containing the row and column coordinates.
    """
    done = False
    while not done:
        try:
            coordinates = input("Enter coordinates: e.g. A1, C7, I9: ")
            column = coordinates[0]
            row = coordinates[1]
            valid_coordinates = validate_coordinates(row, column)
            if valid_coordinates == True:
                done = True
                return row, column
            else:
                print("Invalid input: Coordinates must be between A1 and I9")
        except ValueError:
            print("Invalid input: Enter a letter followed by a number")

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
    not_saved = False
    while not not_saved:
        save_message = input("Do you want to save the game? (y/n): ")
        if save_message.lower() == "y":
            override_message = input("Save to an new file or override the current file? (n/c): ")
            if override_message.lower() == "n":
                new_filename = input("Enter a new filename: ")
                with open(new_filename, 'w') as file:
                    json.dump(board, file)
                    not_saved = True
            elif override_message.lower() == "c":
                with open(current_filename, 'w') as file:
                    json.dump(board, file)
                    not_saved = True
            else:
                print("Invalid input: Enter 'n' or 'c'")

    

def get_input_value(board, row, column):
    """
    Prompt the user for a value and return it.
    
    The function ensures that the provided value is valid. It will 
    repeatedly ask for input until a valid input is provided.
    
    Parameters:
        board (list of lists of int): The current state of the Sudoku board.
        row (int): The row coordinate of the cell to edit.
        column (str): The column coordinate of the cell to edit.
        
    Returns:
        str: The value provided by the user.
    """
    valid = False
    while not valid:
        value = input("Specify a coordinate to edit, enter 'S' to recive a hint of valid enteries, or 'Q' to save and quit ")
        if validate_input_value(board, row, column, value):
            valid = True
            return value
        else:
            print("Invalid input: Enter a number between 1 and 9, 's' for a hint, or 'q' to quit and save")

def handle_input_value(board, filename, row, column, value):
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
        display_hint_options(board, row, column)
    elif value.lower() == "q":
        save_game(board, filename)
    else:
        update_board(board, row, column, value)

def validate_input_value(value):
    """
    Validate whether the provided input value is within acceptable bounds or commands.
    
    Parameters:
        value (str): The value provided by the user.
        
    Returns:
        bool: True if the input value is valid, False otherwise.
    """
    if value >= 1 or value <= 9 or value.lower() == "s" or value.lower() == "q":
        return True
    else:
        return False

def display_hint_options(board, row, column, value):
    """
    Display possible valid entries for the specified Sudoku cell.
    
    Parameters:
        board (list of lists of int): The current state of the Sudoku board.
        row (int): The row coordinate of the cell.
        column (str): The column coordinate of the cell.
        value (str): The value to validate as a hint.
    """
    hint_options = []

    


    print(f"Hint options for {column}{row}: {hint_options}")

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
    
    display_board(board)
    row, column = get_coordinates()
    if DEBUG:
        print(row, column)
    value = get_input_value(board, row, column)
    handle_input_value(board, filename, row, column, value)
    display_board(board)
    
        

def main():
    
    
    # filename = get_filename()
    if TEST:
        filename = "demo.json"
    board = read_board(filename)
    play_game(board, filename)

if __name__ == "__main__":
    main()
import os.path
import json

DEBUG = True
TEST = True

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
    done = False
    while not done:
        try:
            coordinates = input("Enter coordinates: e.g. A1, C7, I9: ")
            column = coordinates[0]
            row = int(coordinates[1])
            valid_coordinates = validate_coordinates(row, column)
            if valid_coordinates == True:
                done = True
                return row, column
            else:
                print("Invalid input: Coordinates must be between A1 and I9")
        except ValueError:
            print("Invalid input: Enter a letter followed by a number")

def validate_coordinates(row, column):
    if row >= 1 or row <= 9 and column >= "A" or column <= "I":
        return True
    else:
        return False
    

def save_game(board, current_filename):
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
    valid = False
    while not valid:
        value = input("Specify a coordinate to edit, enter 'S' to recive a hint of valid enteries, or 'Q' to save and quit ")
        if validate_input_value(board, row, column, value):
            valid = True
            return value
        else:
            print("Invalid input: Enter a number between 1 and 9, 's' for a hint, or 'q' to quit and save")

def handle_input_value(board, filename, row, column, value):
    if value.lower() == "s":
        display_hint_options(board, row, column)
    elif value.lower() == "q":
        save_game(board, filename)
    else:
        update_board(board, row, column, value)

def validate_input_value(value):
    if value >= 1 or value <= 9 or value.lower() == "s" or value.lower() == "q":
        return True
    else:
        return False

def display_hint_options(board, row, column):
    hint_options = []
    for i in range(1, 10):
        if i not in board[row]:
            hint_options.append(i)
    print(f"Valid options for row {row} are {hint_options}")
    for i in range(1, 10):
        if i not in board[column]:
            hint_options.append(i)
    print(f"Valid options for column {column} are {hint_options}")
    for i in range(1, 10):
        if i not in board[row] and i not in board[column]:
            hint_options.append(i)
    print(f"Valid options for square {row}, {column} are {hint_options}")



def update_board(board, row, column, value):
    board[row][column] = value
    update_board = board

    return update_board

    


def play_game(board, filename):
    """
    Play a game of Sudoku interactively with the user.

    Parameters:
        board (list): The Sudoku board.
    """
    
    display_board(board)
    row, column = get_coordinates()
    if DEBUG:
        print(row, column)
    save_game(board, filename)
    value = get_input_value(board, row, column)
    handle_input_value(board, filename, row, column, value)
    display_board(board)
    
        

def main():
    
    
    # filename = get_filename()
    if TEST:
        filename = "demo.json"
    board = read_board(filename)
    play_game(board)

if __name__ == "__main__":
    main()
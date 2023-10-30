import os.path
import json

def get_filename():
    """Prompts the user for a filename and return it."""
    while True:
        filename = input("Enter a filename: ")
        if os.path.isfile(filename):
            return filename
        print("File does not exist.")

def read_board(filename):
    """Reads a Sudoku board from the specified file and return a board."""
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
    """Displays the Sudoku board in a user-friendly format."""
    print("   A B C D E F G H I")
    for row in range(9):
        if row == 3 or row == 6:
            print("   -----+-----+-----")
        print(f"{row + 1}  ", end="")
        for column in range(9):
            separator = "|" if column == 2 or column == 5 else " "
            print(f"{board[row][column] or ' '}{separator}", end="")
        print()

def get_coordinates():
    """Prompt the user for cell coordinates or to quit."""
    while True:
        coordinates = input("Specify a coordinate (e.g. A1, C7, I9, B2) or 'Q' to save and quit: ").upper()
        if len(coordinates) == 2 and coordinates[0].isdigit() and coordinates[1].isalpha():
            coordinates = coordinates[1] + coordinates[0]
        if coordinates == 'Q' or (len(coordinates) == 2 and 'A' <= coordinates[0] <= 'I' and '1' <= coordinates[1] <= '9'):
            return coordinates
        print("Invalid coordinates.")

def get_cell_value():
    """Prompt the user for a cell value, hint request, or to quit."""
    value = input("Enter a number (1-9), 'S' for a hint, or 'Q' to save and quit: ").upper()
    while not (value in ['S', 'Q'] or (value.isdigit() and 1 <= int(value) <= 9)):
        print("Invalid input.")
        value = input("Enter a number (1-9), 'S' for a hint, or 'Q' to save and quit: ").upper()
    return value

def is_valid_move(game_board, row, col, number):
    """Check if a move is valid and return a list of reasons or True if valid."""
    reasons = []
    
    if number in game_board[row]:
        reasons.append("row")
    if number in [game_board[i][col] for i in range(9)]:
        reasons.append("column")
        
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for inner_row in range(3):
        for inner_col in range(3):
            if game_board[start_row + inner_row][start_col + inner_col] == number:
                reasons.append("square")
                
    if not reasons:
        return True
    else:
        return reasons


def get_hint_options(board, row, column):
    """Get possible valid entries for the specified Sudoku cell."""
    hint_options = []
    position_value = board[row][column]
    if position_value != 0:
        return hint_options
    for num in range(1, 10):
        if is_valid_move(board, row, column, num) == True:
            hint_options.append(num)
    return hint_options

def update_board(game_board, row, col, value):
    """Update the specified cell in the Sudoku board with the provided value."""
    game_board[row][col] = value

def play_game(game_board, file_path):
    """Main game loop."""
    game_over = False
    while not game_over:
        display_board(game_board)
        coordinates = get_coordinates()
        if coordinates == 'Q':
            save_game(game_board, file_path)
            game_over = True
        elif game_board[ord(coordinates[0]) - ord('A')][int(coordinates[1]) - 1]:
            print(f"The cell '{coordinates}' is already filled.")
        else:
            row, col = ord(coordinates[0]) - ord('A'), int(coordinates[1]) - 1
            value_received = False
            while not value_received:
                value = get_cell_value()
                if value == 'Q':
                    save_game(game_board, file_path)
                    game_over = True
                    value_received = True
                elif value == 'S':
                    hint_options = get_hint_options(game_board, row, col)
                    print(f"Hints for {coordinates}: {hint_options}")
                else:
                    valid_or_reasons = is_valid_move(game_board, row, col, int(value))
                    if valid_or_reasons == True:
                        update_board(game_board, row, col, int(value))
                        value_received = True
                    else:
                        reasons = valid_or_reasons
                        print(f"{value} is not a valid move for {coordinates} because it's already in the {reasons}. Try again or enter 'S' for a hint.")

def save_game(game_board, file_path):
    """Save the current game state to a file."""
    choice = input("Save to the current file or a new file? (C/N): ").upper()
    if choice == 'N':
        file_path = input("Enter a new filename: ")
    with open(file_path, 'w') as file:
        json.dump({"board": game_board}, file)

def test_is_valid_move():
    """Test the is_valid_move function."""
    board = read_board("test.json")
    assert is_valid_move(board, 0, 0, 1) == True
    assert is_valid_move(board, 0, 9, 1) == True
    assert is_valid_move(board, 9, 0, 1) == True
    assert is_valid_move(board, 5, 5, 1) == True


if __name__ == "__main__":

    if __debug__:
        test_is_valid_move()
    filename = get_filename()
    board = read_board(filename)
    play_game(board, filename)


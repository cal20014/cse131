import os.path
import json

def get_filename():
    """
    Prompts the user for a filename and return it.
    """
    while True:
        user_filename = input("Enter a filename: ")
        if os.path.isfile(user_filename):
            return user_filename
        print("File does not exist.") 

def read_board(file_path):
    """
    Reads a Sudoku board from the specified file and return a board.
    """
    try:
        with open(file_path, 'r') as file:
            board_data = json.load(file)
            sudoku_board = board_data['board']
        return sudoku_board
    except FileNotFoundError:
        print(f"No such file or directory: '{file_path}'")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file: '{file_path}'")

def display_board(sudoku_board):
    """
    Displays the Sudoku board in a user-friendly format.
    """
    print("   A B C D E F G H I")
    
    for row_index, row in enumerate(sudoku_board):
        if row_index in [3, 6]:
            print("   -----+-----+-----")
        print(f"{row_index + 1}  ", end="")

        for col_index, cell in enumerate(row):
            separator = "|" if col_index in [2, 5] else " "
            print(f"{cell or ' '}{separator}", end="")
        print()

def get_coordinates():
    """Prompt the user for cell coordinates or to quit."""
    while True:
        user_input = input("Specify a coordinate (e.g. A1, C7, I9, B2) or 'Q' to save and quit: ").upper()
        if len(user_input) == 2 and user_input[0].isdigit() and user_input[1].isalpha():
            user_input = user_input[1] + user_input[0]
        if user_input == 'Q':
            return None
        if len(user_input) == 2 and 'A' <= user_input[0] <= 'I' and '1' <= user_input[1] <= '9':
            return ord(user_input[0]) - ord('A'), int(user_input[1]) - 1
        print("Invalid coordinates.")

def get_cell_value():
    """Prompt the user for a cell value, hint request, or to quit."""
    while True:
        value = input("Enter a number (1-9), 'S' for a hint, or 'Q' to save and quit: ").upper()
        if value in ['S', 'Q'] or (value.isdigit() and 1 <= int(value) <= 9):
            return value
        print("Invalid input.")

def is_valid_move(sudoku_board, row, col, number):
    """Check if a move is valid."""
    for index in range(9):
        if sudoku_board[row][index] == number or sudoku_board[index][col] == number:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for inner_row in range(3):
        for inner_col in range(3):
            if sudoku_board[start_row + inner_row][start_col + inner_col] == number:
                return False
    return True


def get_hints(sudoku_board, row, col):
    """Return a list of valid numbers for a cell."""
    return [num for num in range(1, 10) if is_valid_move(sudoku_board, row, col, num)]

def play_game(sudoku_board, file_path):
    """Main game loop."""
    while True:
        display_board(sudoku_board)
        coords = get_coordinates()
        if coords is None:
            save_game(sudoku_board, file_path)
            break
        row, col = coords
        if sudoku_board[row][col]:
            print("Cell is already filled.")
            continue
        while True:
            value = get_cell_value()
            if value == 'Q':
                save_game(sudoku_board, file_path)
                return
            elif value == 'S':
                print(f"Hints for {chr(col + ord('A'))}{row + 1}: {', '.join(map(str, get_hints(sudoku_board, row, col)))}")
            elif is_valid_move(sudoku_board, row, col, int(value)):
                sudoku_board[row][col] = int(value)
                break
            else:
                print(f"{value} is not a valid move for {chr(col + ord('A'))}{row + 1}. Try again or enter 'S' for a hint.")

def save_game(sudoku_board, file_path):
    """Save the current game state to a file."""
    choice = input("Save to the current file or a new file? (C/N): ").upper()
    if choice == 'N':
        file_path = input("Enter a new filename: ")
    with open(file_path, 'w') as file:
        json.dump({"board": sudoku_board}, file)

if __name__ == "__main__":
    file_path = get_filename()
    sudoku_board = read_board(file_path)
    play_game(sudoku_board, file_path)

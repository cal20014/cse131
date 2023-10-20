import os.path
import json

def get_filename():
    """
    Prompts the user for a filename and return it.
    
    The function repeatedly prompts the user until an existing file is provided. 
    
    Returns:
        str: The filename provided by the user.
    """
    while True:
        filename = input("Enter a filename: ")
        if os.path.isfile(filename):
            return filename
        print("File does not exist.") 

def read_board(filename):
    """
    Reads a Sudoku board from the specified file.
    
    Parameters:
        filename (str): The path to the JSON file.
        
    Returns:
        list of lists of integers: The Sudoku board.
    """
    with open(filename, 'r') as file:
        return json.load(file)['board']

def display_board(board):
    """Displays the Sudoku board."""
    print("   A B C D E F G H I")
    for i, row in enumerate(board):
        if i in [3, 6]:
            print("   -----+-----+-----")
        print(f"{i + 1}  " + " ".join(str(cell) if cell else ' ' for cell in row[:3]) +
              "|" + " ".join(str(cell) if cell else ' ' for cell in row[3:6]) +
              "|" + " ".join(str(cell) if cell else ' ' for cell in row[6:]))

def get_coordinates():
    """Prompt the user for cell coordinates or to quit."""
    while True:
        coords = input("Specify a coordinate (e.g. A1, C7, I9) or 'Q' to save and quit: ").upper()
        if coords == 'Q':
            return None
        if len(coords) == 2 and 'A' <= coords[0] <= 'I' and '1' <= coords[1] <= '9':
            return ord(coords[0]) - ord('A'), int(coords[1]) - 1
        print("Invalid coordinates.")

def get_value():
    """Prompt the user for a cell value, hint request, or to quit."""
    while True:
        value = input("Enter a number (1-9), 'S' for a hint, or 'Q' to save and quit: ").upper()
        if value in ['S', 'Q'] or (value.isdigit() and 1 <= int(value) <= 9):
            return value
        print("Invalid input.")

def is_valid_move(board, row, col, num):
    """Check if a move is valid."""
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def get_hints(board, row, col):
    """Return a list of valid numbers for a cell."""
    return [num for num in range(1, 10) if is_valid_move(board, row, col, num)]

def play_game(board, filename):
    """Main game loop."""
    while True:
        display_board(board)
        coords = get_coordinates()
        if coords is None:
            save_game(board, filename)
            break
        row, col = coords
        if board[row][col]:
            print("Cell is already filled.")
            continue
        value = get_value()
        if value == 'Q':
            save_game(board, filename)
            break
        elif value == 'S':
            print(f"Hints for {chr(col + ord('A'))}{row + 1}: {', '.join(map(str, get_hints(board, row, col)))}")
        elif is_valid_move(board, row, col, int(value)):
            board[row][col] = int(value)
        else:
            print(f"{value} is not a valid move for {chr(col + ord('A'))}{row + 1}.")

def save_game(board, filename):
    """Save the current game state to a file."""
    choice = input("Save to the current file or a new file? (C/N): ").upper()
    if choice == 'N':
        filename = input("Enter a new filename: ")
    with open(filename, 'w') as file:
        json.dump({"board": board}, file)

if __name__ == "__main__":
    filename = get_filename()
    board = read_board(filename)
    play_game(board, filename)

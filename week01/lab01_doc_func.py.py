import json

# Constants for Tic-Tac-Toe characters.
X = 'X'
O = 'O'
BLANK = ' '

# Initial turn variable
turn = 0

# Initial blank Tic-Tac-Toe board.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(filename):
    """
    Read the board state from a file.

    Parameters:
    - filename (str): The name of the file to read the board from.

    Returns:
    - list: The board state. Returns a blank board if the file doesn't exist.
    """
    try:
        with open(filename, "r") as file_handle:
            json_data = file_handle.read()
            dictionary_data = json.loads(json_data)
            return dictionary_data
    except:
        print(f"There was an error. The file: {filename} could not be found")
        return blank_board['board']

def save_board(filename, board):
    """
    Save the current game board state to a file.

    Parameters:
    - filename (str): The name of the file to save the board to.
    - board (list): The current state of the board.
    """
    try:
        with open(filename, "w") as file_handle:
            json_data = json.dumps(board)
            file_handle.write(json_data)
    except:
        print(f"There was an error. The file: {filename} could not be found")

def display_board(board):
    """
    Display the current state of the Tic-Tac-Toe board.

    Parameters:
    - board (list): The current state of the board.
    """
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def is_x_turn(board):
    """
    Determine whose turn it is.

    Parameters:
    - board (list): The current state of the board.

    Returns:
    - bool: True if it's X's turn, False otherwise.
    """
    return board.count(X) <= board.count(O)

def get_current_turn(board):
    """
    Determine whose turn it is.

    Parameters:
    - board (list): The current state of the board.

    Returns:
    - str: Returns 'X' or 'O' based on whose turn it is.
    """
    return X if is_x_turn(board) else O

def get_player_choice(board):
    """
    Get the player's choice from input.

    Returns:
    - str: Returns the player's choice.
    """
    return input(f"{get_current_turn(board)}> ").strip()

def update_board(board, player_choice, current_turn):
    """
    Updates the board based on the player's choice.

    Parameters:
    - board (list): The current state of the board.
    - player_choice (int): The player's choice for the move.
    - current_turn (str): Current player's turn ('X' or 'O').

    Returns:
    - bool: Returns True if the board was updated successfully, False otherwise.
    """
    if 0 <= int(player_choice) <= 9:
        if board[player_choice - 1] == BLANK:
            board[player_choice - 1] = current_turn
            return True
        else:
            print("That spot has already been taken. Choose a different spot.")
            return False
    else:
        print(f"Invalid input: {player_choice} is not correct.")
        print("please choose a number between 1-9")
        return False

def check_game_status(board):
    """
    Checks if the game is finished.

    Parameters:
    - board (list): The current state of the board.

    Returns:
    - bool: Returns True if the game is finished, False otherwise.
    """
    if game_done(board):
        display_board(board)
        game_done(board, message=True)
        save_board("game_board.json", blank_board["board"])
        return True
    return False

def play_game(board):
    """
    The main game loop for playing Tic-Tac-Toe.

    Parameters:
    - board (list): The current state of the board.

    Returns:
    - bool: False if the user quits the game, True if the game finishes normally.
    """
    while True:
        display_board(board)
        current_turn = get_current_turn(board)
        player_choice = get_player_choice()

        if player_choice.lower() == "q":
            save_board("game_board.json", board)
            print("The Game was saved!")
            print("run the game again to start where you left off")
            return False

        if update_board(board, player_choice, current_turn):
            if check_game_status(board):
                return True


def game_done(board, message=False):
    """
    Determine if the game is finished.

    Parameters:
    - board (list): The current state of the board.
    - message (bool, optional): If True, display a message about the game's outcome.

    Returns:
    - bool: True if the game is over, False otherwise.
    """
    # Check for a winning row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print(f"The game was won by {board[row * 3]}!")
            return True

    # Check for a winning column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print(f"The game was won by {board[col]}!")
            return True

    # Check for a winning diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or board[2] == board[4] == board[6]):
        if message:
            print(f"The game was won by {board[4]}!")
        return True

    # Check for a tie.
    if all(square != BLANK for square in board):
        if message:
            print("The game is a tie!")
        return True

    return False

def info_display_message():
    """
    Display instructions and information for the user about how to play the game.
    """
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
    Main function to start and run the game.
    """
    info_display_message()
    board = read_board("game_board.json")
    play_game(board)

if __name__ == "__main__":
    main()

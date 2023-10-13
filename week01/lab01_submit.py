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

# Help references: Brother Godderidge, 
# https://docs.python.org/3/library/json.html, Brother Barzee.
# Doc string style help comes from previous semester help from Brother Helfrich,
# Brother Barzee, and ai style assistace (chatgpt).

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
    Reads the current board from a file.

    Parameters:
    - filename (str): The name of the file to read the board from.

    Returns:
    - The the current board. Returns a blank board if the file doesn't exist.
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
    Saves the current game board to a file.

    Parameters:
    - filename (str): The name of the file to save the board to.
    - board: The current game board.
    """
    try:
        with open(filename, "w") as file_handle:
            json_data = json.dumps(board)
            file_handle.write(json_data)
    except:
        print(f"There was an error. The file: {filename} could not be found")

def display_board(board):
    """
    Displays the current state of the Tic-Tac-Toe board.

    Parameters:
    - board: The current game board.
    """
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def is_x_turn(board):
    """
    Determines whose turn it is.

    Parameters:
    - board: The current game board.

    Returns:
    - True if it's X's turn, False otherwise.
    """
    return board.count(X) <= board.count(O)

def play_game(board):
    """
    The main game loop for playing Tic-Tac-Toe.

    Parameters:
    - board: The current game board.

    Returns:
    False if the user quits the game, True if the game finishes normally.
    """
    while True:
        display_board(board)

        # Determine whose turn it is.
        if is_x_turn(board):
            current_turn = X
        else:
            current_turn = O


        player_choice = input(f"{current_turn}> ").strip()

        if player_choice.lower() == "q":
            save_board("game_board.json", board)
            print("The Game was saved!")
            print("run the game again to start where you left off")
            return False

        try:
            if 1 <= int(player_choice) <= 9:
                player_choice = int(player_choice)

                # Check if the chosen spot is available.
                if board[player_choice - 1] == BLANK:
                    board[player_choice - 1] = current_turn

                    if game_done(board):
                        display_board(board)
                        game_done(board, message=True)
                        save_board("game_board.json", blank_board["board"])
                        return True
                else:
                    print("That spot has already been taken. Choose a different spot.")
            else:
                print(f"Invalid input: {player_choice} is not a valid input.")
                print("please choose a number between 1-9")
        except:
            print(f"Invalid input: {player_choice} is not a valid input.")
            print("please choose a number between 1-9")

def game_done(board, message=False):
    """
    Determines if the game is finished.

    Parameters:
    - board: The current game board.
    - message: If True, display a message about the game's outcome.

    Returns:
    - True if the game is over, False otherwise.
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
    Displays instructions for the user about how to play the game.
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
    - Displays start message.
    - Reads in a the previous game.
    - Begins the game.
    """
    info_display_message()
    board = read_board("game_board.json")
    play_game(board)

if __name__ == "__main__":
    main()

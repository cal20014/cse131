import json

# The characters used in the Tic-Tac-Toe board.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data['board']
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return blank_board['board']

def save_board(filename, board):
    '''Save the current game to a file.'''
    data = {"board": board}
    with open(filename, 'w') as file:
        json.dump(data, file)

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def is_x_turn(board):
    '''Determine whose turn it is.'''
    return board.count(X) == board.count(O)

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    while True:
        # Display the board
        display_board(board)
        
        # Determine whose turn it is
        current_player = X if is_x_turn(board) else O
        
        # Get player input with prompt and remove any whitespace that might cause and error.
        choice = input(f"{current_player}> ").strip()
        
        # If the player chooses to quit
        if choice == 'q':
            save_board("saved_game.json", board)
            print("Game saved.")
            return False
        
        # If the player makes a valid move
        if choice.isdigit() and 1 <= int(choice) <= 9:
            choice = int(choice)
            if board[choice - 1] == BLANK:
                board[choice - 1] = current_player
                
                # Check if the game is done
                if game_done(board, message=False):  # Temporarily set message to False
                    display_board(board)  # Display the board after the winning move
                    game_done(board, message=True)  # Display the winning message
                    save_board("saved_game.json", blank_board['board'])
                    return True
            else:
                print("That spot is already taken!")
        else:
            print("Invalid choice. Please select a number from 1 to 9.")


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
    

def main():
    # User instructions
    print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
    print("where the following numbers correspond to the locations on the grid:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")
    print("The current board is:")

    # Main game loop
    board = read_board("saved_game.json")
    play_game(board)

if __name__ == "__main__":
    main()

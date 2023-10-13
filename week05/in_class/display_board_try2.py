import json

def read_board(filename="demo.json"):
    with open(filename, "r") as myFile:
        myData = myFile.read()
        # print(myData)
        # print(type(myData))
        parsed_data = json.loads(myData)
        board = parsed_data["board"]
        return board

# Function to display the Sudoku board without using enumerate
def display_board(board):
    print("try#1")
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # print horizontal line after every 3 rows
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")  # print vertical line after every 3 columns
            print(board[i][j] if board[i][j] != 0 else " ", end=" ")  # print number or . for 0
        print()  # go to the next line after each row

def display_enu_board(board):
    print("try#32")
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-"*21)  # print horizontal line after every 3 rows
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")  # print vertical line after every 3 columns
            print(num if num != 0 else ".", end=" ")  # print number or . for 0
        print()  # go to the next line after each row

# Function to display the Sudoku board
def display_heading_board(board):
    print("try#3")
    print("   A B C D E F G H I")
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("   -----+-----+-----")
        print(f"{i+1} ", end=" ")
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else " ", end=" ")
        print()

# Function to display the Sudoku board using enumerate
def display_heading_enu_board(board):
    print("try#4")
    print("   A B C D E F G H I")
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("   -----+-----+-----")
        print(f"{i+1} ", end=" ")
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(num if num != 0 else " ", end=" ")
        print()


def main():
    board = read_board("demo.json")
    display_board(board)
    display_enu_board(board)
    display_heading_board(board)
    display_heading_enu_board(board)


if __name__ == "__main__":
    main()  
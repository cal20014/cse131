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
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # print horizontal line after every 3 rows
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")  # print vertical line after every 3 columns
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")  # print number or . for 0
        print()  # go to the next line after each row


def main():
    board = read_board("game_board.json")
    display_board(board)


def display_auto_board(board):
    pass
    



  

# def display_manual_board(board):
#     """
#     Displays the Sudoku board
    
#     """
#     for data in myDict["board"]:
#         for num in data:
#             if num == 0:
#                 num = " "
#             else:
#                 num = num
    
#     print(f"{board[0][0]} {board[0][1]} {board[0][2]} | {board[0][3]} {board[0][4]} {board[0][5]} | {board[0][6]} {board[0][7]} {board[0][8]}")
#     print(f"{board[1][0]} {board[1][1]} {board[1][2]} | {board[1][3]} {board[1][4]} {board[1][5]} | {board[1][6]} {board[1][7]} {board[1][8]}")
#     print(f"{board[2][0]} {board[2][1]} {board[2][2]} | {board[2][3]} {board[2][4]} {board[2][5]} | {board[2][6]} {board[2][7]} {board[2][8]}")
#     print("------+-------+------")
#     print(f"{board[3][0]} {board[3][1]} {board[3][2]} | {board[3][3]} {board[3][4]} {board[3][5]} | {board[3][6]} {board[3][7]} {board[3][8]}")
#     print(f"{board[4][0]} {board[4][1]} {board[4][2]} | {board[4][3]} {board[4][4]} {board[4][5]} | {board[4][6]} {board[4][7]} {board[4][8]}")
#     print(f"{board[5][0]} {board[5][1]} {board[5][2]} | {board[5][3]} {board[5][4]} {board[5][5]} | {board[5][6]} {board[5][7]} {board[5][8]}")
#     print("------+-------+------")
#     print(f"{board[6][0]} {board[6][1]} {board[6][2]} | {board[6][3]} {board[6][4]} {board[6][5]} | {board[6][6]} {board[6][7]} {board[6][8]}")
#     print(f"{board[7][0]} {board[7][1]} {board[7][2]} | {board[7][3]} {board[7][4]} {board[7][5]} | {board[7][6]} {board[7][7]} {board[7][8]}")
#     print(f"{board[8][0]} {board[8][1]} {board[8][2]} | {board[8][3]} {board[8][4]} {board[8][5]} | {board[8][6]} {board[8][7]} {board[8][8]}")
    


# for index in range(0, len(board))


# display_board(myDict["board"])

# display_board(board)
# ______THIS ARE GLOBAL VARIABLES____
# _____@_ANKIT'S CREATION____
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
player = "X"
winner = None
game_still_going = True

# this is the board of the game.


def display_board():
    global board
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])

# this is the main game function which controls everything sequentially.


def main_game():
    display_board()

    while game_still_going:
        handel_turn(player)

        game_over()

        switch_player()

    if winner == "X" or winner == "O":
        print(f"{winner} won the game :)")

    elif winner == None:
        print("the match was a tie :(")

# this is an important function which takes the imput from the player and looks after many didderent things like
# whether the input is valid or the position of the input is either avaiable or not.


def handel_turn(new_player):
    global board
    global player
    print(f"{new_player}'s turn now!! ")
    s = input("enter a positon where you want to place your piece: ")
    valid = True
    while valid:
        while s not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            s = input(
                "enter a valid positon where you want to place your piece: ")
        s = int(s)-1
        if board[s] == "-":
            valid = False
        else:
            print("you can't go there go again")

    board[s] = new_player
    display_board()


#  used for checking the curent status of the game.
def game_over():
    check_for_winner()
    check_if_tie()

# this function is only used for assigning the winner of the rows,coloumns and diagonals.


def check_for_winner():
    global winner

    row_winner = check_rows()
    coloumm_winner = check_coloumns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif coloumm_winner:
        winner = coloumm_winner
    elif diagonal_winner:
        winner = diagonal_winner

# this check rows,coloumns and diagonals function are used fot two purposes that are 1)geting out of the game loop.
# 2) returning the winner to the check winner function and assigning the winner.


def check_rows():
    global board
    global game_still_going
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        game_still_going = False

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]


def check_diagonals():
    global board
    global game_still_going
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"
    if diagonal1 or diagonal2:
        game_still_going = False

    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]


def check_coloumns():
    global board
    global game_still_going
    coloumn1 = board[0] == board[3] == board[6] != "-"
    coloumn2 = board[1] == board[4] == board[7] != "-"
    coloumn3 = board[2] == board[5] == board[8] != "-"

    if coloumn1 or coloumn2 or coloumn3:
        game_still_going = False

    if coloumn1:
        return board[0]
    elif coloumn2:
        return board[1]
    elif coloumn3:
        return board[2]

# used for switching the player


def switch_player():
    global player
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"

# this is used to check whether the game is tie or not


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False


main_game()

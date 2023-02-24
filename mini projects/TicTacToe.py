import random
board =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

#Taken squares so that a user or the computer does not randomly select a taken square
taken_squares = [5]
square_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Displays the board
def display_board():
    board[1][1] = "X"
    print(f"""    +-------+-------+-------+
    |       |       |       |
    |   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
    |       |       |       |
    +-------+-------+-------+""")

#user enters move
def enter_move():
    move = 0
    while move not in range(1, 10) or move in taken_squares:
        move = int(input("Enter move here: "))
        if move in taken_squares:
            print("That square sis already taken. Please choose another one.")
        if move not in range(1,10):
            print("move not in range")
    taken_squares.append(move)
    row = (move - 1) // 3
    col = (move - 1) % 3
    board[row][col] = "O"
    display_board()


#A def so that a user can see the free spaces
def free_squares():
    print(taken_squares)


#draw move is computer drawing its move
def draw_move():
    move = 0
    while move not in range(1, 10) or move in taken_squares:
        move = random.randint(1,9)
        if move in taken_squares:
            print("That square is already taken. Please choose another one.")
    taken_squares.append(move)
    row = (move - 1) // 3
    col = (move - 1) % 3
    board[row][col] = "X"
    display_board()

def check_winner():
    if board[0][0] == board [0][1] == board[0][2]:
        return(board[0][0])
    elif board[1][0] == board [1][1] == board[1][2]:
        return(board[1][0])
    elif board[2][0] == board [2][1] == board[2][2]:
        return(board[2][0])
    elif board[0][0] == board [1][0] == board[2][0]:
        return(board[0][0])
    elif board[0][1] == board [1][1] == board[2][1]:
        return(board[0][1])
    elif board[0][2] == board [1][2] == board[2][2]:
        return(board[0][2])
    elif board[0][0] == board [1][1] == board[2][2]:
        return(board[0][1])
    elif board[0][2] == board [1][1] == board[2][0]:
        return(board[0][2])
while True:
    display_board()
    enter_move()
    winner = check_winner()
    draw_move()
    winner = check_winner()
    if winner == "X":
        print("Computer won!")
        break
    elif winner == "O":
        print("You win!")
    elif len(taken_squares) == 9:
        print("Draw")
        break

        


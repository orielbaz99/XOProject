# game board
board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

playing = True
turn = 'X'



# displays the board
def displayBoard():
    for row in board:
        print(row)



def playGame():
    displayBoard()

    for i in range(9):
        handleTurn()


def handleTurn():
    global playing
    global count
    while playing:
        print(f"\n* {turn}'s turn *")
        chooseRow = int(input('\nchoose row :'))
        chooseColumn = int(input('choose column :'))

        if board[chooseRow][chooseColumn] == '_':
            board[chooseRow][chooseColumn] = turn
        elif board[chooseRow][chooseColumn] != '_':
            print('\n***   this place is taken ! try again   ***\n')
            not flipPlayer()

        displayBoard()
        if gameOver():
            playing = False
        else:
            flipPlayer()


# checks if the game is over
def gameOver():
    if winGame():
        print('*****   Game Over !   *****')
        return True
    elif tieGame():
        return True
    else:
        return False


# checks for tie
def tieGame():
    global count
    global board
    tie = True
    for row in board:
        if '_' in row:
            tie = False

    if tie:
        print("\n*** It's a Tie ! ***")
        print('\n*** Game Over ! ***')
        return True
    else:
        return False


# checks for win by different ways
def winGame():
    if rowsWin() or columnsWin() or diagonalsWin():
        return True
    else:
        return False


# flips between X and O
def flipPlayer():
    global turn
    if turn == 'X':
        turn = 'O'
    elif turn == 'O':
        turn = 'X'


def rowsWin():
    global turn
    if board[0][0] == board[0][1] == board[0][2] != "_":
        print(f'\n*****   Winner is {turn} !   ***** \n')
        return True

    elif board[1][0] == board[0][1] == board[0][2] != "_":
        print(f'\n*****   Winner is {turn} !   ***** \n')
        return True

    elif board[2][0] == board[2][1] == board[2][2] != "_":
        print(f'\n*****   Winner is {turn} !   ***** \n')
        return True
    else:
        return False


def columnsWin():
    if board[0][0] == board[1][0] == board[2][0] != "_":
        print(f'\n*****   Winner is {turn} !   ***** \n')
        return True

    elif board[0][1] == board[1][1] == board[2][1] != "_":
        print(f'\n*****   Winner is {turn} !   ***** \n')
        return True

    elif board[0][2] == board[1][2] == board[2][2] != "_":
        print(f'\n*****   Winner is {turn} !   ***** \n')
        return True


def diagonalsWin():
    if board[0][0] == board[1][1] == board[2][2] != "_":
        print(f'\n*****   Winner is {turn} !   ***** \n')
        return True
    elif board[0][2] == board[1][1] == board[2][0] != "_":
        print(f'\n*****   Winner is {turn} !   ***** \n')
        return True


playGame()

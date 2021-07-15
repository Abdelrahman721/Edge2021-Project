

def showBoard():
    print("-------------------------------")
    for r in board:
        for c in r:
            print(c,end = "    ")
        print()
        print()
    print("-------------------------------")
    print("0    1    2    3    4    5    6")


def placePiece(column, player):

    if column > 6 or column < 0:
        print("Choose a different column")
        return False

    if board[0][column] != "-":
        print("Choose a different column")
        return False

    for i in range(6):
        if board[5-i][column] == "-":
            board[5-i][column] = player
            break

    return True


def playFriend():
    counter = 0
    player = ""
    while True:
        counter += 1
        if counter % 2 != 0:
            player = "1"
            showBoard()
            column = int(input("(P1) Choose a column: "))
            if placePiece(column, player) == False:
                counter -= 1
                continue
            if gameOverP1( ) == True:
                showBoard()
                break
        else:
            player = "2"
            showBoard()
            column = int(input("(P2) Choose a column: "))
            placePiece(column, player)
            if gameOverP2( )== True:
                showBoard()
                break


def gameOverP1():

    for i in range(len(board)):
        for j in range(4):
            if board[i][j]=="1" and board[i][j+1]=="1" and board[i][j+2]=="1" and board[i][j+3]=="1":
                print("Player 1 Won!")
                return True

    for j in range (len(board[0])):
        for i in range(3):
            if board[i][j]=="1" and board[i+1][j]=="1" and board[i+2][j]=="1" and board[i+3][j]=="1":
                print("Player 1 Won!")
                return True

    for i in [5,4,3]:
        for j in range(4):
            if board[i][j]=="1" and board[i-1][j+1]=="1" and board[i-2][j+2]=="1" and board[i-3][j+3]=="1":
                print("Player 1 Won!")
                return True

    for i in [5,4,3]:
        for j in [6,5,4,3]:
            if board[i][j]=="1" and board[i-1][j-1]=="1" and board[i-2][j-2]=="1" and board[i-3][j-3]=="1":
                print("Player 1 Won!")
                return True
    return False


def gameOverP2():

    for i in range(len(board)):
        for j in range(4):
            if board[i][j]=="1" and board[i][j+1]=="1" and board[i][j+2]=="1" and board[i][j+3]=="1":
                print("Player 2 Won!")
                return True

    for j in range (len(board[0])):
        for i in range(3):
            if board[i][j]=="1" and board[i+1][j]=="1" and board[i+2][j]=="1" and board[i+3][j]=="1":
                print("Player 2 Won!")
                return True

    for i in [5,4,3]:
        for j in range(4):
            if board[i][j]=="1" and board[i-1][j+1]=="1" and board[i-2][j+2]=="1" and board[i-3][j+3]=="1":
                print("Player 2 Won!")
                return True

    for i in [5,4,3]:
        for j in [6,5,4,3]:
            if board[i][j]=="1" and board[i-1][j-1]=="1" and board[i-2][j-2]=="1" and board[i-3][j-3]=="1":
                print("Player 2 Won!")
                return True
    return False


def main():
    choice = 0
    while True:
        print("\nHello there! Please choose an option to begin the game.")
        choice = int(input("\n0. Exit the game (press 0)\n1. Play a friend (press 1)\n2. Play the computer (press 2)\n"))
        if choice == 1:
            playFriend()
        elif choice == 2:
            playComp()
        elif choice == 0:
          return
        else:
            print("Invalid choice - Retry a different option")


board = [["-"]*7 for _ in range(6)]
main()





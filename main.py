def printBoard(xState, zState):
    board = []
    for i in range(9):
        if xState[i]:
            board.append('X')
        elif zState[i]:
            board.append('O')
        else:
            board.append(str(i))

    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"--|---|---")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"--|---|---")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def checkWin(state):
    winPatterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6]              # diagonal
    ]
    for pattern in winPatterns:
        if state[pattern[0]] and state[pattern[1]] and state[pattern[2]]:
            return True
    return False


if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for X, 0 for O

    print("Welcome to Tic Tac Toe")
    while True:
        printBoard(xState, zState)
        if turn == 1:
            print("X's turn")
            value = int(input("Please enter a value: "))
            if xState[value] == 0 and zState[value] == 0:
                xState[value] = 1
                turn = 0
                if checkWin(xState):
                    print("X wins!")
                    break
            else:
                print("Invalid move, try again.")
        else:
            print("O's turn")
            value = int(input("Please enter a value: "))
            if xState[value] == 0 and zState[value] == 0:
                zState[value] = 1
                turn = 1
                if checkWin(zState):
                    print("O wins!")
                    break
            else:
                print("Invalid move, try again.")

        if all(xState) or all(zState):
            print("It's a draw!")
            break
    printBoard(xState, zState)
    print("Game Over!")

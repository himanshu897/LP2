def printSolution(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=' ')
        print()

def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solveNQUtil(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQUtil(board, col + 1):
                return True
            board[i][col] = 0
    return False

def solveNQ():
    N = int(input("Enter the value of N: "))
    board = [[0] * N for _ in range(N)]
    if not solveNQUtil(board, 0):
        print("Solution does not exist")
        return False
    print("Solution:")
    printSolution(board)
    return True

while True:
    print("1. Solve N-Queens problem")
    print("2. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        solveNQ()
    elif choice == "2":
        break
    else:
        print("Invalid choice. Please try again.\n")

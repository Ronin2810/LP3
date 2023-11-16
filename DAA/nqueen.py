def is_safe(board, row, col, n):
    # Check if no other Queen is present in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row, n):
    if row == n:
        # If all Queens are placed successfully, print the board
        for i in range(n):
            for j in range(n):
                if(board[i][j]==0):
                    print("_", end=" ")
                else:
                    print("Q",end=" ")
            print()
        print()
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place the Queen

            # Recur for the next row
            solve_n_queens(board, row + 1, n)

            # Backtrack and remove the Queen
            board[row][col] = 0

def place_queens_with_first_queen(board, n, first_queen_row):
    # Solve for the remaining Queens starting from the second column (column index 1)
    solve_n_queens(board, 0, n)

# Example usage:
n = 7  # Change this to the desired number of Queens
first_queen_row = 1  # Change this to the desired row for the first Queen
board = [[0] * n for _ in range(n)]
place_queens_with_first_queen(board, n, first_queen_row)

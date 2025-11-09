# N-Queens Problem using Backtracking

def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print()

# Check if a queen can be placed safely at board[row][col]
def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

# Solve N-Queens using backtracking
def solve_nqueens(board, row, n):
    if row == n:
        print_solution(board, n)
        return True

    found_solution = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            found_solution = solve_nqueens(board, row + 1, n) or found_solution
            board[row][col] = 0  # Backtrack

    return found_solution

# ------------- MAIN PROGRAM -------------
n = int(input("Enter the number of queens: "))
board = [[0 for _ in range(n)] for _ in range(n)]

# Place first queen at a fixed position (optional)
first_col = int(input(f"Enter column (0 to {n-1}) to place first queen in row 0: "))
board[0][first_col] = 1

print("\nAll possible solutions are:\n")
solve_nqueens(board, 1, n)

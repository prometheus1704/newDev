def print_solution(board,n):
    for i in range(n):
        row=""
        for j in range(n):
            row+=' Q ' if board[i][j] else " . "
        print(row)
    print("\n"+"-"*30)

def solve_nQueens(n):
    board=[[0 for _ in range(n)]for _ in range(n)]
    col=[False]*(n)
    diag1=[False]*(2*n)
    diag2=[False]*(2*n)
    solutions=[]

    def backtrack(row):
        if row==n:
            board_copy=[row.copy() for row in board]
            solutions.append(board_copy)
            return

        for c in range(n):
            # Branch and Bound check:
            if not col[c] and not diag1[row+c] and not diag2[row-c+n]:
                board[row][c]=1
                col[c]=diag1[row+c]=diag2[row-c+n]=True
                
                backtrack(row+1)

                board[row][c]=0
                col[c]=diag1[row+c]=diag2[row-c+n]=False
    backtrack(0)

    print(f"total no of solutions: {len(solutions)}")
    for sol in solutions:
        print_solution(sol,n)
        
n = int(input("Enter the number of queens (n): "))
solve_nQueens(n)
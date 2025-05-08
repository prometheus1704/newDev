import heapq

class State:
    def __init__(self, board, g=0):
        self.board = board  # board[i] = column of queen in row i
        self.g = g  # Number of queens placed so far
        self.h = self.heuristic()  # Heuristic: number of conflicting queen pairs

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

    def heuristic(self):
        """Counts the number of attacking queen pairs"""
        h = 0
        n = len(self.board)
        for i in range(n):
            for j in range(i + 1, n):
                if self.board[i] == self.board[j] or abs(self.board[i] - self.board[j]) == j - i:
                    h += 1
        return h

    def is_goal(self):
        """Check if all 8 queens are placed without conflict"""
        return len(self.board) == 8 and self.h == 0

    def get_neighbors(self):
        """Generates possible next states by placing a queen in the next row"""
        next_row = len(self.board)
        neighbors = []
        for col in range(8):
            # Only check diagonals and verticals
            conflict = False
            for r in range(next_row):
                c = self.board[r]
                if c == col or abs(col - c) == abs(next_row - r):
                    conflict = True
                    break
            if not conflict:
                new_board = self.board + [col]
                neighbors.append(State(new_board, self.g + 1))
        return neighbors


def a_star_8_queens(first_queen_row, first_queen_col):
    """Solves the 8-queens problem using A* with the first queen fixed"""
    open_list = []
    initial_state = State([first_queen_col])  # Start with the first queen fixed

    heapq.heappush(open_list, initial_state)

    visited = set()  # To avoid revisiting same state

    while open_list:
        current = heapq.heappop(open_list)

        if tuple(current.board) in visited:
            continue
        visited.add(tuple(current.board))

        if current.is_goal():
            return current.board  # Solution found

        for neighbor in current.get_neighbors():
            if tuple(neighbor.board) not in visited:
                heapq.heappush(open_list, neighbor)

    return None  # No solution found (should never happen for 8-queens)


# Take user input for the first queen's position
first_row = int(input("Enter the row for the first queen (0-7): "))
first_col = int(input("Enter the column for the first queen (0-7): "))

# Run the A* algorithm
solution = a_star_8_queens(first_row, first_col)

if solution:
    print("\nSolution:", solution)
    for row in range(8):
        line = ["Q" if solution[row] == col else "." for col in range(8)]
        print(" ".join(line))
else:
    print("No solution found.")

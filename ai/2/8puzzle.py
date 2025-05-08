import heapq

MOVES = {
    "DOWN": (-1, 0),
    "UP": (1, 0),
    "RIGHT": (0, -1),
    "LEFT": (0, 1),
}

class PuzzleState:
    def __init__(self, board, parent=None, move=None, moved_tile=None, g=0, h=0):
        self.board = board
        self.parent = parent
        self.move = move  
        self.moved_tile = moved_tile
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

def manhattan_distance(board, goal):
    """Calculate Manhattan distance heuristic."""
    distance = 0
    for r in range(3):
        for c in range(3):
            if board[r][c] != 0:
                value = board[r][c]
                goal_r, goal_c = next((gr, gc) for gr in range(3) for gc in range(3) if goal[gr][gc] == value)
                distance += abs(goal_r - r) + abs(goal_c - c)
    return distance

def find_blank(board):
    """Find the (row, col) of the blank space (0)."""
    for r in range(3):
        for c in range(3):
            if board[r][c] == 0:
                return r, c

def generate_successors(state, goal):
    """Generate possible moves from current state."""
    successors = []
    blank_r, blank_c = find_blank(state.board)
    for move, (dr, dc) in MOVES.items():
        new_r, new_c = blank_r + dr, blank_c + dc
        if 0 <= new_r < 3 and 0 <= new_c < 3:
            new_board = [row[:] for row in state.board]
            moved_tile = new_board[new_r][new_c]
            new_board[blank_r][blank_c], new_board[new_r][new_c] = new_board[new_r][new_c], new_board[blank_r][blank_c]
            h = manhattan_distance(new_board, goal)
            successors.append(PuzzleState(new_board, state, move, moved_tile, state.g + 1, h))
    return successors

def reconstruct_path(state):
    """Reconstruct the path from the initial to goal state."""
    path = []
    while state:
        path.append((state.board, state.move, state.moved_tile))
        state = state.parent
    return path[::-1]

def a_star(initial, goal):
    """A* Algorithm to solve the 8-puzzle problem."""
    initial_state = PuzzleState(initial, None, None, None, 0, manhattan_distance(initial, goal))
    frontier = []
    heapq.heappush(frontier, initial_state)
    explored = set()

    while frontier:
        current = heapq.heappop(frontier)
        if current.board == goal:
            return reconstruct_path(current)

        explored.add(tuple(map(tuple, current.board)))
        for successor in generate_successors(current, goal):
            if tuple(map(tuple, successor.board)) not in explored:
                heapq.heappush(frontier, successor)

    return None

def print_board(board):
    """Print the 2D board in a readable format."""
    for row in board:
        print(" ".join(str(cell) if cell != 0 else "_" for cell in row))
    print()

if __name__ == "__main__":
    print("Enter initial state (row-wise, 3x3, use 0 for blank):")
    initial = [list(map(int, input().split())) for _ in range(3)]
    
    print("Enter goal state (row-wise, 3x3, use 0 for blank):")
    goal = [list(map(int, input().split())) for _ in range(3)]

    print("\nSolving 8-puzzle using A* algorithm...\n")
    solution = a_star(initial, goal)

    if solution:
        for i, (board, move, moved_tile) in enumerate(solution):
            if move:
                print(f"Step {i}: Move tile {moved_tile} {move}")
            else:
                print("Initial state:")
            print_board(board)
    else:
        print("No solution found.")

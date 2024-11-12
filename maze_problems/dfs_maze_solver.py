def is_valid_move(maze, x, y, visited):
    # Check if the move is within bounds and not a wall or visited
    return (0 <= x < len(maze)) and (0 <= y < len(maze[0])) and maze[x][y] == 0 and not visited[x][y]


def dfs(maze, x, y, dest, visited):
    # If the current position is the destination, return True (found a path)
    if (x, y) == dest:
        return True

    # Mark the current cell as visited
    visited[x][y] = True

    # Possible moves: down, up, right, left
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for move in moves:
        next_x, next_y = x + move[0], y + move[1]
        if is_valid_move(maze, next_x, next_y, visited):
            if dfs(maze, next_x, next_y, dest, visited):
                return True

    # Backtrack (unmark this cell)
    visited[x][y] = False
    return False


# Maze solving function
def solve_maze(maze, start, destination):
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    return dfs(maze, start[0], start[1], destination, visited)


# Example maze
mazes = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

st = (0, 0)
dst = (4, 4)

if solve_maze(mazes, st, dst):
    print("Path found!")
else:
    print("No path found.")

import matplotlib.pyplot as plt
from matplotlib import colors
from PIL import Image
import numpy as np

def is_valid_move(maze, x, y, visited):
    # Check if the move is within bounds and not a wall or visited
    return (0 <= x < len(maze)) and (0 <= y < len(maze[0])) and maze[x][y] == 0 and not visited[x][y]

# DFS helper function to generate frames
def dfs_with_animation(maze, x, y, destination, visited, path, frames):
    # If the current position is the destination, return True and append the final frame
    if (x, y) == destination:
        path.append((x, y))
        frames.append(visualize_maze(maze, path))  # Capture final frame
        return True

    # Mark the current cell as visited and capture frame
    visited[x][y] = True
    path.append((x, y))
    frames.append(visualize_maze(maze, path))  # Capture current frame

    # Possible moves: down, up, right, left
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for move in moves:
        next_x, next_y = x + move[0], y + move[1]
        if is_valid_move(maze, next_x, next_y, visited):
            if dfs_with_animation(maze, next_x, next_y, destination, visited, path, frames):
                return True

    # Backtrack (unmark this cell and capture frame)
    visited[x][y] = False
    path.pop()
    frames.append(visualize_maze(maze, path))  # Capture backtrack frame
    return False


# Visualize the current state of the maze
def visualize_maze(maze, path):
    # Create a color map (0=white, 1=black for walls, and a different color for the path)
    cmap = colors.ListedColormap(['white', 'black', 'red'])
    maze_copy = np.array(maze, dtype=int)

    # Mark the path on the maze
    for (x, y) in path:
        maze_copy[x][y] = 2

    fig, ax = plt.subplots()
    ax.imshow(maze_copy, cmap=cmap)
    ax.set_xticks([])
    ax.set_yticks([])

    # Save the figure as a frame
    fig.canvas.draw()
    img = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    plt.close(fig)

    return img


# Convert the frames to GIF using Pillow
def save_gif(frames, filename="maze_solution.gif"):
    images = [Image.fromarray(frame) for frame in frames]
    images[0].save(
        filename, save_all=True, append_images=images[1:], duration=200, loop=0
    )


# Main maze solving function
def solve_maze_with_gif(maze, start, destination):
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    path = []
    frames = []

    dfs_with_animation(maze, start[0], start[1], destination, visited, path, frames)

    # Save the animation as a GIF
    save_gif(frames, "maze_solution.gif")


# Example maze
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
destination = (4, 4)

# Solve the maze and create the GIF
solve_maze_with_gif(maze, start, destination)

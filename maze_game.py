import numpy as np
import random

def generate_maze(size):
    maze = np.zeros_like(np.zeros((size, size)), dtype=int)
    for i in range(size):
        for j in range(size):
            if random.random() < 0.3:
                maze[i][j] = 1
    return maze

def print_maze(maze):
    for row in maze:
        print(" ".join("⬛" if cell == 0 else "⬜" for cell in row))

print("Generated Maze:")
maze = generate_maze(10)
print_maze(maze)

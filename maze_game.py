import numpy as np
import random
import os
import time


def player(maze, player_row, player_col):
    maze[player_row][player_col] = 2
    return maze


def generate_maze(size):
    maze = np.zeros((size, size), dtype=int)

    for i in range(size):
        for j in range(size):
            if random.random() < 0.3:
                maze[i][j] = 1

    # Make sure starting position isn't a wall
    maze[0][0] = 0

    return maze


def print_maze(maze):
    for row in maze:
        print("".join(
            "⬛" if cell == 1 else
            "⬜" if cell == 0 else
            "🟦"
            for cell in row
        ))

    print()
    print("Controls: W = Up | A = Left | S = Down | D = Right")


def controls(player_row, player_col):
    move = input("Move (WASD): ").lower()

    new_row = player_row
    new_col = player_col

    if move == "w":
        new_row -= 1

    elif move == "s":
        new_row += 1

    elif move == "a":
        new_col -= 1

    elif move == "d":
        new_col += 1

    else:
        print("Please use W, A, S or D.")

    return new_row, new_col


def main():
    size = 15
    maze = generate_maze(size)
    player_row = 0
    player_col = 0
    maze = player(maze, player_row, player_col)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_maze(maze)
        new_row, new_col = controls(player_row, player_col)

        if (0 <= new_row < size and 0 <= new_col < size):
            if maze[new_row][new_col] != 1:
                maze[player_row][player_col] = 0

                player_row = new_row
                player_col = new_col
                maze = player(maze,player_row,player_col)

        else:
            print("You can't move outside the maze!")
            time.sleep(0.3)


main()

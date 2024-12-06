import numpy as np
import pandas as pd


directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def read_lines(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()


def step(terrain, position, direction):
    next_position = position + directions[direction]
    try:
        if terrain[next_position[0], next_position[1]] == "#":
            direction = (direction + 1) % 4
            next_position = position + directions[direction]
    except IndexError:
        pass
    return next_position, direction


def part_one():
    terrain = np.array([list(line) for line in read_lines("./06/06.txt")])
    x, y = np.where(terrain == "^")
    position = np.array((x[0], y[0]))
    direction = 0
    while np.all(position >= 0) and np.all(position < len(terrain)):
        terrain[position[0], position[1]] = "X"
        position, direction = step(terrain, position, direction)
    visited_positions = (terrain == "X").sum()

    print(f"Visited positions: {visited_positions}")


def part_two():
    terrain = np.array([list(line) for line in read_lines("./06/06.txt")])
    terrain_copy = np.copy(terrain)
    x, y = np.where(terrain == "^")

    position = np.array((x[0], y[0]))
    direction = 0

    while np.all(position >= 0) and np.all(position < len(terrain)):
        terrain[position[0], position[1]] = "X"
        position, direction = step(terrain, position, direction)
    visited_positions = np.where((terrain == "X"))
    xs, ys = visited_positions

    possible_obstruction_spots = 0
    for x0, y0 in zip(xs, ys):
        position = np.array((x[0], y[0]))
        direction = 0

        custom_terrain = np.copy(terrain_copy)
        custom_terrain[x0, y0] = "#"
        times_visited = np.zeros(terrain.shape)

        while np.all(position >= 0) and np.all(position < len(custom_terrain)):
            times_visited[position[0], position[1]] += 1
            if times_visited[position[0], position[1]] > 3:
                possible_obstruction_spots += 1
                break
            position, direction = step(custom_terrain, position, direction)

    print(f"Number of possible obstruction spots: {possible_obstruction_spots}")


if __name__ == "__main__":
    part_one()
    part_two()

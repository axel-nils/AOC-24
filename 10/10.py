import numpy as np
import pandas as pd


def read_lines(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line


def get_von_neumann_neighbors(matrix_shape, i, j):
    rows, cols = matrix_shape
    top = max(i - 1, 0)
    bottom = min(i + 1, rows - 1)
    left = max(j - 1, 0)
    right = min(j + 1, cols - 1)

    neighbor_rows = [top, bottom, i, i]
    neighbor_cols = [j, j, left, right]
    return zip(neighbor_rows, neighbor_cols)


def dfs(matrix, i, j, current_value, max_value, reachable):
    # Base case
    if matrix[i, j] != current_value:
        return

    # If search complete
    if current_value == max_value:
        reachable.add((i, j))
        return

    # Recurse
    next_value = current_value + 1
    for ni, nj in get_von_neumann_neighbors(matrix.shape, i, j):
        dfs(matrix, ni, nj, next_value, max_value, reachable)


def dfs2(matrix, i, j, current_value, max_value):
    # Base case
    if matrix[i, j] != current_value:
        return 0

    # If search complete
    if current_value == max_value:
        return 1

    # Recurse
    next_value = current_value + 1
    count = 0
    for ni, nj in get_von_neumann_neighbors(matrix.shape, i, j):
        count += dfs2(matrix, ni, nj, next_value, max_value)

    return count


def part_one():
    height_map = np.array(
        [list(line.strip()) for line in read_lines("./10/10.txt")], dtype=int
    )
    trailheads = np.where(height_map == 0)
    total_count = []
    for i, j in zip(trailheads[0], trailheads[1]):
        reachable = set()
        dfs(height_map, i, j, 0, 9, reachable)
        total_count.append(len(reachable))

    print(f"Sum of scores of all trailheads: {sum(total_count)}")


def part_two():
    height_map = np.array(
        [list(line.strip()) for line in read_lines("./10/10.txt")], dtype=int
    )
    trailheads = np.where(height_map == 0)
    total_count = []
    for i, j in zip(trailheads[0], trailheads[1]):
        count = dfs2(height_map, i, j, 0, 9)
        total_count.append(count)

    print(f"Sum of ratings of all trailheads: {sum(total_count)}")


if __name__ == "__main__":
    part_one()
    part_two()

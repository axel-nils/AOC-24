import numpy as np
import pandas as pd


def read(file_path):
    df = pd.read_csv(file_path, sep="\\s+", header=None)
    return df


def read_lines(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()


def part_one():
    antinodes = set()
    antenna_map = np.array([list(line) for line in read_lines("./08/08.txt")])
    m = antenna_map.shape[0]
    frequencies = np.unique(antenna_map)
    filtered_frequencies = frequencies[frequencies != "."]

    for f in filtered_frequencies:
        x, y = np.where(antenna_map == f)
        f_locations = np.array([p for p in zip(x, y)])

        vectors = 2 * f_locations[np.newaxis, :, :] - f_locations[:, np.newaxis, :]
        n = f_locations.shape[0]
        corresponding_antinodes = {
            tuple(vectors[i, j])
            for i in range(n)
            for j in range(n)
            if i != j and np.all(vectors[i, j] >= 0) and np.all(vectors[i, j] < m)
        }
        antinodes.update(corresponding_antinodes)

    print(f"Number of antinodes found 2 steps away: {len(antinodes)}")


def part_two():
    antinodes = set()
    antenna_map = np.array([list(line) for line in read_lines("./08/08.txt")])
    m = antenna_map.shape[0]
    frequencies = np.unique(antenna_map)
    filtered_frequencies = frequencies[frequencies != "."]

    for f in filtered_frequencies:
        x, y = np.where(antenna_map == f)
        f_locations = np.array([p for p in zip(x, y)])
        for k in range(m):
            vectors = k * f_locations[np.newaxis, :, :] + (1 - k) * f_locations[:, np.newaxis, :]
            n = f_locations.shape[0]
            corresponding_antinodes = {
                tuple(vectors[i, j])
                for i in range(n)
                for j in range(n)
                if np.all(vectors[i, j] >= 0) and np.all(vectors[i, j] < m)
            }
            antinodes.update(corresponding_antinodes)

    print(f"Number of antinodes found any number of steps away: {len(antinodes)}")


if __name__ == "__main__":
    part_one()
    part_two()

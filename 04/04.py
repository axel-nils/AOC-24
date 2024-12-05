import numpy as np
import pandas as pd
import itertools as it


def read_lines(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line


def part_one():
    lines = read_lines("./04/04.txt")
    char_mat = np.array([list(s.strip("\n")) for s in lines])
    x_locs = np.where(char_mat == "X")
    x_ij = np.array(x_locs).T

    rows, cols = char_mat.shape
    directions = np.array(list(it.product(range(-1, 2), repeat=2)))

    xmas_counter = 0
    for l in x_ij:
        valid_directions = np.all(
            (l + 3 * directions >= 0) & (l + 3 * directions < cols), axis=1
        )  # assuming char_mat square
        for d in directions[valid_directions]:
            m_ij = l + d
            s_ij = l + d * 3
            a_ij = l + d * 2
            m = char_mat[m_ij[0], m_ij[1]]
            a = char_mat[a_ij[0], a_ij[1]]
            s = char_mat[s_ij[0], s_ij[1]]
            if m == "M" and a == "A" and s == "S":
                xmas_counter += 1
    print(f"Number of occurances of XMAS : {xmas_counter}")


def part_two():
    lines = read_lines("./04/04.txt")
    char_mat = np.array([list(s.strip("\n")) for s in lines])
    a_locs = np.where(char_mat == "A")
    a_ij = np.array(a_locs).T

    rows, cols = char_mat.shape
    directions = np.array(list(it.product([-1, 1], repeat=2)))

    mas_counter = np.zeros(char_mat.shape)
    for l in a_ij:
        if np.all((l - 1 >= 0) & (l + 1 < cols)):  # assuming char_mat square
            for d in directions:
                m_ij = l - d
                s_ij = l + d
                m = char_mat[m_ij[0], m_ij[1]]
                s = char_mat[s_ij[0], s_ij[1]]
                if m == "M" and s == "S":
                    mas_counter[l[0], l[1]] += 1

    xmas_counter = np.count_nonzero(mas_counter == 2)  # two overlapping MASs
    print(f"Number of occurances of X-MAS : {xmas_counter}")


if __name__ == "__main__":
    part_one()
    part_two()

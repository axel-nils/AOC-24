import numpy as np
import pandas as pd


def read_lines(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line


def check_safe(levels):
    diff = np.diff(levels)
    if np.any(diff == 0) or np.any(diff > 3) or np.any(diff < -3):
        return False
    else:
        return np.all(diff > 0) or np.all(diff < 0)


def part_one():
    safe = 0
    for line in read_lines("02/02.txt"):
        levels = np.fromstring(line, sep=" ")
        if check_safe(levels):
            safe += 1

    print(f"With strict rules: {safe} reports are safe")


def part_two():
    safe = 0
    for line in read_lines("02/02.txt"):
        levels = np.fromstring(line, sep=" ")
        if check_safe(levels):
            safe += 1
        else:
            for i in range(len(levels)):
                modified_levels = np.delete(levels, i)
                if check_safe(modified_levels):
                    safe += 1
                    break

    print(f"With lenient rules: {safe} reports are safe")


if __name__ == "__main__":
    part_one()
    part_two()

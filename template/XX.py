import numpy as np
import pandas as pd


def read(file_path):
    df = pd.read_csv(file_path, sep="\\s+", header=None)
    return df


def read_lines(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line


def part_one():
    pass


def part_two():
    pass


if __name__ == "__main__":
    part_one()
    part_two()

import numpy as np
import pandas as pd


def read_lines(file_path):
    with open(file_path, "r") as file:
        return file.readline().strip()


def part_one():
    disk_map = np.array(list(read_lines("./09/09.txt")), dtype=int)
    disk_blocks = np.zeros(disk_map.sum())

    j = 0
    m = 0
    for i, n in enumerate(disk_map):
        if i % 2 == 0:
            disk_blocks[j : j + n + 1] = m
            j += n
            m += 1
        else:
            disk_blocks[j : j + n + 1] = -1
            j += n

    l, r = np.min(np.where(disk_blocks == -1)), np.max(np.where(disk_blocks != -1))
    while l < r:
        disk_blocks[r], disk_blocks[l] = disk_blocks[l], disk_blocks[r]
        l, r = np.min(np.where(disk_blocks == -1)), np.max(np.where(disk_blocks != -1))

    p = np.arange(l)
    checksum = int(np.sum(p * disk_blocks[p]))
    print(f"Checksum after moving individual blocks: {checksum}")


def part_two():
    disk_map = np.array(list(read_lines("./09/ex.txt")), dtype=int)
    disk_blocks = np.zeros(disk_map.sum())

    j = 0
    m = 0
    for i, n in enumerate(disk_map):
        if i % 2 == 0:
            disk_blocks[j : j + n + 1] = m
            j += n
            m += 1
        else:
            disk_blocks[j : j + n + 1] = -1
            j += n

    ids = np.array(np.unique(disk_blocks[disk_blocks != -1]), dtype=int)
    for id in ids[::-1]:
        if id % 100 == 0:
            print(id)
        s = np.sum(disk_blocks == id)
        l, r = np.min(np.where(disk_blocks == -1)), np.min(np.where(disk_blocks == id))
        for i in range(l, r - s):
            if np.all(disk_blocks[i : i + s] == -1):
                disk_blocks[r : r + s], disk_blocks[i : i + s] = (
                    disk_blocks[i : i + s].copy(),
                    disk_blocks[r : r + s].copy(),
                )
                break

    p = np.arange(disk_blocks.size)
    valid_p = p[disk_blocks != -1]
    checksum = int(np.sum(valid_p * disk_blocks[valid_p]))
    print(f"Checksum after moving entire files: {checksum}")


if __name__ == "__main__":
    # part_one()
    part_two()

import numpy as np
import pandas as pd
import re


def read(file_path):
    with open(file_path, "r") as file:
        data = file.read().replace("\n", "")
    return data


def part_one():
    program = read("./03/03.txt")

    mul_pattern = r"mul\((?P<X>\d+),(?P<Y>\d+)\)"
    instructions = re.finditer(mul_pattern, program)

    products = map(lambda i: int(i.group("X")) * int(i.group("Y")), instructions)
    sum = np.sum(list(products))
    print(f"The sum resulting from the valid instructions is: {sum}")


def part_two():
    program = read("./03/03.txt")

    do_mul_pattern = r"mul\((?P<X>\d+),(?P<Y>\d+)\)|do\(\)|don't\(\)"
    instructions = re.finditer(do_mul_pattern, program)

    do = True
    sum = 0
    for i in instructions:
        match i.group(0):
            case "do()":
                do = True
            case "don't()":
                do = False
            case _:
                if do:
                    sum += int(i.group("X")) * int(i.group("Y"))

    print(f"The sum when consider do() or don't() is: {sum}")


if __name__ == "__main__":
    part_one()
    part_two()

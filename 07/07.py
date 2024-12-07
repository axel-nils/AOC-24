from itertools import product
from functools import reduce


add = lambda a, b: int(a) + int(b)
mul = lambda a, b: int(a) * int(b)
cat = lambda a, b: int(str(a) + str(b))


def read_lines(file_path):
    with open(file_path, "r") as file:
        for line in file:
            result, operands = line.strip().split(":")
            yield result.strip(), operands.strip().split(" ")


def part_one():
    eqs = read_lines("./07/07.txt")
    sum = 0
    for result, operands in eqs:
        perms = product([add, mul], repeat=(len(operands) - 1))
        for operations in perms:
            attempt = reduce(
                lambda acc, pair: pair[1](acc, pair[0]),
                zip((operands[1:]), operations),
                int(operands[0]),
            )
            if attempt == int(result):
                sum += attempt
                break
    
    print(f"Total calibration result using [+, *]: {sum}")


def part_two():
    eqs = read_lines("./07/07.txt")
    sum = 0
    for result, operands in eqs:
        perms = product([add, mul, cat], repeat=(len(operands) - 1))
        for operations in perms:
            attempt = reduce(
                lambda acc, pair: pair[1](acc, pair[0]),
                zip((operands[1:]), operations),
                int(operands[0]),
            )
            if attempt == int(result):
                sum += attempt
                break
    
    print(f"Total calibration result using [+, *, ||]: {sum}")


if __name__ == "__main__":
    part_one()
    part_two()

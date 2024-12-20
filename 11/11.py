def read_values(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        values = list(map(int, content.split()))
    return values


def solve(stone, blinks, mem):
    if blinks == 0:
        return 1
    elif (stone, blinks) in mem:
        return mem[(stone, blinks)]
    elif stone == 0:
        val = solve(1, blinks - 1, mem)
    elif len(str_stone := str(stone)) % 2 == 0:
        mid = len(str_stone) // 2
        left = solve(int(str_stone[:mid]), blinks - 1, mem)
        right = solve(int(str_stone[mid:]), blinks - 1, mem)
        val = left + right
    else:
        val = solve(stone * 2024, blinks - 1, mem)
    mem[(stone, blinks)] = val
    return val


def part_one():
    starting_stones = read_values("./11/11.txt")
    memory = {}
    numer_of_stones = 0
    total_blinks = 25

    for value in starting_stones:
        numer_of_stones += solve(value, total_blinks, memory)

    print(f"Number of stones after {total_blinks} blinks: {numer_of_stones}")


def part_two():
    starting_stones = read_values("./11/11.txt")
    memory = {}
    numer_of_stones = 0
    total_blinks = 75

    for value in starting_stones:
        numer_of_stones += solve(value, total_blinks, memory)

    print(f"Number of stones after {total_blinks} blinks: {numer_of_stones}")


if __name__ == "__main__":
    part_one()
    part_two()

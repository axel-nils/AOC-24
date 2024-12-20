import numpy as np
from collections import defaultdict


def read_values(file_path):
    with open(file_path, "r") as file:
        for line in file:
            values = list(line.strip())
            yield values


def add_to_dict_with_duplicates(regions, key, coord, neighbor=None):
    if key not in regions:
        regions[key].append([coord])
    else:
        added = False
        for sublist in regions[key]:
            if neighbor in sublist:
                sublist.append(coord)
                added = True
        if not added:
            regions[key].append([coord])


def merge_sublists(sublists):
    changed = True
    while changed:  # Keep merging until no changes
        changed = False
        merged = []
        while sublists:
            current = sublists.pop(0)
            # Find and merge all overlapping sublists
            overlapping = [s for s in sublists if any(elem in current for elem in s)]
            if overlapping:
                for overlap in overlapping:
                    current.extend(overlap)
                    sublists.remove(overlap)
                changed = True  # A merge occurred
            # Remove duplicates and add to merged list
            merged.append(list(set(current)))
        sublists = merged  # Start again with merged sublists
    return sublists


def calculate_perimeter(coordinates):
    coordinate_set = set(coordinates)
    perimeter = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for x, y in coordinates:
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)
            if neighbor not in coordinate_set:
                perimeter += 1

    return perimeter


def count_distinct_sides(coordinates):
    coord_set = set(coordinates)

    top_edges = []
    bottom_edges = []
    left_edges = []
    right_edges = []

    for x, y in coordinates:
        if (x, y + 1) not in coord_set:
            top_edges.append((x, y))
        if (x, y - 1) not in coord_set:
            bottom_edges.append((x, y))
        if (x - 1, y) not in coord_set:
            left_edges.append((x, y))
        if (x + 1, y) not in coord_set:
            right_edges.append((x, y))

    def find_distinct_edges(edge_cells, is_vertical):
        if not edge_cells:
            return []

        # Sort cells appropriately
        if is_vertical:
            edge_cells.sort(key=lambda p: (p[0], p[1]))  # Sort by x then y
        else:
            edge_cells.sort(key=lambda p: (p[1], p[0]))  # Sort by y then x

        distinct_edges = []
        current_edge = [edge_cells[0]]

        for cell in edge_cells[1:]:
            prev_cell = current_edge[-1]

            # Check if cells are adjacent and align properly
            if is_vertical:
                same_edge = cell[0] == prev_cell[0] and cell[1] == prev_cell[1] + 1
            else:
                same_edge = cell[1] == prev_cell[1] and cell[0] == prev_cell[0] + 1
            if same_edge:
                current_edge.append(cell)
            else:
                distinct_edges.append(current_edge)
                current_edge = [cell]

        distinct_edges.append(current_edge)
        return distinct_edges

    # Find distinct edges in each direction
    distinct_top = find_distinct_edges(top_edges, False)
    distinct_bottom = find_distinct_edges(bottom_edges, False)
    distinct_left = find_distinct_edges(left_edges, True)
    distinct_right = find_distinct_edges(right_edges, True)

    total_edges = (
        len(distinct_top)
        + len(distinct_bottom)
        + len(distinct_left)
        + len(distinct_right)
    )

    return total_edges


def form_regions(filepath):
    farm = np.array(list(read_values(filepath)))
    rows, cols = farm.shape
    regions = defaultdict(list)
    for i in range(rows):
        for j in range(cols):
            crop = farm[i, j]
            loc = (i, j)
            if i > 0 and crop == farm[i - 1, j]:
                add_to_dict_with_duplicates(regions, crop, loc, (i - 1, j))
            if j > 0 and crop == farm[i, j - 1]:
                add_to_dict_with_duplicates(regions, crop, loc, (i, j - 1))
            else:
                add_to_dict_with_duplicates(regions, crop, loc)

    for key in regions:
        regions[key] = merge_sublists(regions[key])
    return regions


def part_one(regions):
    cost = 0
    for key in regions:
        for region in regions[key]:
            region_cost = calculate_perimeter(region) * len(region)
            cost += region_cost

    print(f"Price of fencing: {cost}")


def part_two(regions):
    cost = 0
    for key in regions:
        for region in regions[key]:
            region_cost = count_distinct_sides(region) * len(region)
            cost += region_cost

    print(f"Discounted price of fencing: {cost}")


if __name__ == "__main__":
    regions = form_regions("./12/12.txt")
    part_one(regions)
    part_two(regions)

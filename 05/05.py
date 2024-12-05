from collections import defaultdict

import numpy as np
import pandas as pd


def read_lines(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip("\n")


def parse_input(file_path):
    lines = np.array(list(read_lines(file_path)))
    split = np.where(lines == "")[0][0]
    rules = np.array(list(map(lambda x: x.split("|"), lines[0:split])), dtype=np.uint32)
    updates = [
        np.array(u.split(","), dtype=np.uint32) for u in lines[split + 1 : lines.size]
    ]
    return rules, updates


def get_correct_updates(rules, updates):
    correct_updates = []
    incorrect_updates = []
    for j, u in enumerate(updates):
        ok = True
        for i, n in enumerate(u):
            must_be_after = rules[np.where(rules[:, 0] == n)][:, 1]
            must_be_before = rules[np.where(rules[:, 1] == n)][:, 0]
            before = u[0:i]
            after = u[i + 1 : u.size]
            if np.any(np.isin(must_be_before, after)) or np.any(
                np.isin(must_be_after, before)
            ):
                ok = False
                break
        if ok:
            correct_updates.append(j)
        else:
            incorrect_updates.append(j)
    return correct_updates, incorrect_updates


def topological_sort_dfs(nodes, edges):
    node_set = set(nodes)
    filtered_edges = [(a, b) for a, b in edges if a in node_set and b in node_set]

    graph = defaultdict(list)
    for edge in filtered_edges:
        graph[edge[0]].append(edge[1])

    visited = set()
    stack = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)
        stack.append(node)

    for node in nodes:
        if node not in visited:
            dfs(node)

    return stack[::-1]


def part_one():
    rules, updates = parse_input("./05/05.txt")

    correct_updates, _ = get_correct_updates(rules, updates)

    sum_middle_numbers = np.array(
        [updates[j][len(updates[j]) // 2] for j in correct_updates]
    ).sum()
    print(f"Sum of middle numbers in correct updates: {sum_middle_numbers}")


def part_two():
    rules, updates = parse_input("05/05.txt")

    _, incorrect_updates = get_correct_updates(rules, updates)

    fixed_updates = []
    for j in incorrect_updates:
        fixed_updates.append(topological_sort_dfs(updates[j], rules))

    sum_middle_numbers = np.array(
        [update[len(update) // 2] for update in fixed_updates]
    ).sum()
    print(f"Sum of middle numbers in reordered updates: {sum_middle_numbers}")


if __name__ == "__main__":
    part_one()
    part_two()

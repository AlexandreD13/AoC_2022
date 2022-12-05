"""
Author:         Alexandre Desfosses
Creation date:  2022-12-04
Documentation:

References:
"""


def part1(data: list) -> int:
    data = [elem.rstrip("\n") for elem in data]
    counter = 0
    for line in data:
        left, right = line.split(",")
        l1, l2 = [int(elem) for elem in left.split("-")]
        r1, r2 = [int(elem) for elem in right.split("-")]
        if (min(l1, r1) == l1 and max(l2, r2) == l2) or (min(l1, r1) == r1 and max(l2, r2) == r2):
            counter += 1
    return counter


def part2(data: list) -> int:
    data = [elem.rstrip("\n") for elem in data]
    counter = 0
    for line in data:
        left, right = line.split(",")
        l1, l2 = [int(elem) for elem in left.split("-")]
        r1, r2 = [int(elem) for elem in right.split("-")]
        if (min(l1, r2) == l1 and max(l2, r2) == l2) or (min(r1, l2) == r1 and max(l2, r2) == r2):
            counter += 1
    return counter

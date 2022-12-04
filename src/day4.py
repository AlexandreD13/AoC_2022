"""
Author:         Alexandre Desfosses
Creation date:  2022-12-04
Documentation:

References:
"""

import re


def chunks(data: list, size):
    size = max(1, size)
    return (data[i: i + size] for i in range(0, len(data), size))


def part1(data: list) -> int:
    data = "".join(data).split("\n")
    data = [re.split("[,-]", elem) for elem in data]
    data = [int(elem) for sublist in data for elem in sublist]
    data = chunks(data, 4)
    data = [True for elem in data
            if min(elem[0], elem[2]) == elem[0] and max(elem[1], elem[3]) == elem[1]
            or min(elem[0], elem[2]) == elem[2] and max(elem[1], elem[3]) == elem[3]]
    return len(data)


def part2(data: list) -> int:
    data = "".join(data).split("\n")
    data = [re.split("[,-]", elem) for elem in data]
    data = [int(elem) for sublist in data for elem in sublist]
    data = chunks(data, 4)
    data = [True for elem in data
            if min(elem[0], elem[2]) == elem[0] and max(elem[1], elem[3]) == elem[1]
            or min(elem[0], elem[2]) == elem[2] and max(elem[1], elem[3]) == elem[3]
            or min(elem[0], elem[3]) == elem[0] and min(elem[1], elem[3]) == elem[3]
            or min(elem[0], elem[2]) == elem[0] and min(elem[1], elem[2]) == elem[2]]
    return len(data)

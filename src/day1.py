"""
Author:         Alexandre Desfosses
Creation date:  2022-12-01
Version:        1.0   ->    Creation of file
Documentation:

References:
"""


def part1(data: list) -> int:
    res = "".join(data).split("\n\n")
    res = [elem.split("\n") for elem in res]
    res = [list(map(int, elem)) for elem in res]
    res = [sum(elem) for elem in res]
    res.sort(reverse=True)
    return res[0]


def part2(data: list) -> int:
    res = "".join(data).split("\n\n")
    res = [elem.split("\n") for elem in res]
    res = [list(map(int, elem)) for elem in res]
    res = [sum(elem) for elem in res]
    res.sort(reverse=True)
    return sum(res[0:3])

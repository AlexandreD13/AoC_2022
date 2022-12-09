"""
Author:         Alexandre Desfosses
Creation date:  2022-12-06
Documentation:

References:
"""


def part1(data) -> int:
    data = data[0]
    for i in range(len(data)):
        temp = set(data[i: i + 4])
        if len(temp) == 4:
            return i + 4


def part2(data) -> int:
    data = data[0]
    for i in range(len(data)):
        temp = set(data[i: i + 14])
        if len(temp) == 14:
            return i + 14

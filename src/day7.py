"""
Author:         Alexandre Desfosses
Creation date:  2022-12-07
Documentation:

References:
"""

from collections import defaultdict


def parse_data(data: list) -> defaultdict:
    sizes: defaultdict = defaultdict(int)
    directories: list = []
    for line in data:
        match line.split():
            case [_, _, "/"]:
                directories = []
            case [_, _, ".."]:
                directories.pop()
            case [_, _, elem]:
                directories.append(elem)
            case [elem, _] if elem.isdigit():
                for i in range(len(directories) + 1):
                    path: str = "/" + "/".join(directories[:i])
                    sizes[path] += int(elem)
    return sizes


def part1(data) -> int:
    data = [elem.rstrip("\n") for elem in data]
    sizes: defaultdict = parse_data(data)
    return sum([elem for elem in sizes.values() if elem <= 100000])


def part2(data) -> int:
    data = [elem.rstrip("\n") for elem in data]
    sizes: defaultdict = parse_data(data)
    free_space: int = 70000000 - sizes["/"]
    needed: int = 30000000 - free_space
    return min([elem for elem in sizes.values() if elem >= needed])

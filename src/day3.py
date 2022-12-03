"""
Author:         Alexandre Desfosses
Creation date:  2022-12-03
Documentation:

References:
"""

values: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def part1(data: list) -> int:
    data: list = "".join(data).split("\n")
    data = [list(set(elem[: int((len(elem) / 2))]).intersection(elem[int((len(elem) / 2)):])) for elem in data]
    data = [values.find(elem) + 1 for sublist in data for elem in sublist]
    return sum(data)


def part2(data) -> int:
    res: list = []
    data: list = "".join(data).split("\n")
    data1 = [data[i] for i in range(0, len(data), 3)]
    data2 = [data[i] for i in range(1, len(data), 3)]
    data3 = [data[i] for i in range(2, len(data), 3)]
    for i in range(0, len(data1)):
        for elem in data1[i]:
            if elem in data2[i] and elem in data3[i]:
                res.append(values.find(elem) + 1)
                break
    return sum(res)

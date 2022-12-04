"""
Author:         Alexandre Desfosses
Creation date:  2022-12-04
Documentation:

References:
"""


def part1(data: list) -> int:
    data = "".join(data).split("\n")
    data = [" ".join(" ".join(elem.split("-")).split(",")).split(" ") for elem in data]
    worker1 = [[elem[0], elem[1]] for elem in data]
    worker2 = [[elem[2], elem[3]] for elem in data]
    counter = 0
    for i in range(len(worker1) - 1):
        if min(worker1[i][0], worker2[i][0]) == worker1[i][0] and max(worker1[i][1], worker2[i][1]) == worker2[i][1]\
                or min(worker1[i][0], worker2[i][0]) == worker2[i][0] and max(worker1[i][1], worker2[i][1]) == worker2[i][1]:
            counter += 1
    return counter


def part2(data: list) -> int:
    data = "".join(data).split("\n")
    data = [" ".join(" ".join(elem.split("-")).split(",")).split(" ") for elem in data]
    worker1 = [[elem[0], elem[1]] for elem in data]
    worker2 = [[elem[2], elem[3]] for elem in data]
    counter = 0
    for i in range(len(worker1) - 1):
        if min(worker1[i][0], worker2[i][0]) == worker1[i][0] and max(worker1[i][1], worker2[i][1]) == worker2[i][1]\
                or min(worker1[i][0], worker2[i][0]) == worker2[i][0] and max(worker1[i][1], worker2[i][1]) == worker2[i][1]\
                or min(worker1[i][0], worker2[i][1]) == worker1[i][0] and min(worker1[i][1], worker2[i][1]) == worker2[i][1]\
                or min(worker1[i][0], worker2[i][0]) == worker1[i][0] and min(worker1[i][1], worker2[i][0]) == worker2[i][0]:
            counter += 1
    return counter


# Slightly slower alternative

# def part1(data: list) -> int:
#     data = "".join(data).split("\n")
#     data = [" ".join(" ".join(elem.split("-")).split(",")).split(" ") for elem in data]
#     data = [int(elem) for sublist in data for elem in sublist]
#     data = [data[i: i + 4] for i in range(0, len(data), 4)]
#     data = [True for elem in data
#             if min(elem[0], elem[2]) == elem[0] and max(elem[1], elem[3]) == elem[1]
#             or min(elem[0], elem[2]) == elem[2] and max(elem[1], elem[3]) == elem[3]]
#     return len(data)
#
#
# def part2(data: list) -> int:
#     data = "".join(data).split("\n")
#     data = [" ".join(" ".join(elem.split("-")).split(",")).split(" ") for elem in data]
#     data = [int(elem) for sublist in data for elem in sublist]
#     data = [data[i: i + 4] for i in range(0, len(data), 4)]
#     data = [True for elem in data
#             if min(elem[0], elem[2]) == elem[0] and max(elem[1], elem[3]) == elem[1]
#             or min(elem[0], elem[2]) == elem[2] and max(elem[1], elem[3]) == elem[3]
#             or min(elem[0], elem[3]) == elem[0] and min(elem[1], elem[3]) == elem[3]
#             or min(elem[0], elem[2]) == elem[0] and min(elem[1], elem[2]) == elem[2]]
#     return len(data)

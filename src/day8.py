"""
Author:         Alexandre Desfosses
Creation date:  2022-12-08
Documentation:

References:
"""

# TODO Runtime is too slow, to be reworked


def check_row(data: list, key: tuple) -> (bool, int):
    x, y = key
    length = len(data[y]) - 1
    left_to_x = data[y][0: x]
    left_to_x = [index for index, value in enumerate(left_to_x) if int(value) >= int(data[y][x])]
    x_to_right = data[y][x + 1: len(data[y])]
    x_to_right = [index + 1 for index, value in enumerate(x_to_right) if int(value) >= int(data[y][x])]
    if len(left_to_x) == 0 and len(x_to_right) == 0:
        return True, x * (length - x)
    if len(left_to_x) == 0:
        return True, x * (x_to_right[0])
    if len(x_to_right) == 0:
        return True, (x - left_to_x[-1]) * (length - x)
    return False, (x - left_to_x[-1]) * (x_to_right[0])


def check_column(data: list, key: tuple) -> (bool, int):
    x, y = key
    length = len(data) - 1
    top_to_y = [elem[x] for elem in data][0: y]
    top_to_y = [index for index, value in enumerate(top_to_y) if int(value) >= int(data[y][x])]
    y_to_bottom = [elem[x] for elem in data][y + 1: len(data)]
    y_to_bottom = [index + 1 for index, value in enumerate(y_to_bottom) if int(value) >= int(data[y][x])]
    if len(top_to_y) == 0 and len(y_to_bottom) == 0:
        return True, y * (length - y)
    if len(top_to_y) == 0:
        return True, y * (y_to_bottom[0])
    if len(y_to_bottom) == 0:
        return True, (y - top_to_y[-1]) * (length - y)
    return False, (y - top_to_y[-1]) * (y_to_bottom[0])


def match_patterns(data: list) -> (int, int):
    viewing_score: int = 0
    visible_trees: int = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            match (x, y):
                case (0, _):
                    visible_trees += 1
                case (_, 0):
                    visible_trees += 1
                case (98, _):
                    visible_trees += 1
                case (_, 98):
                    visible_trees += 1
                case other:
                    row = check_row(data, other)
                    column = check_column(data, other)
                    if row[0] or column[0]:
                        visible_trees += 1
                    if row[1] * column[1] > viewing_score:
                        viewing_score = row[1] * column[1]
    return visible_trees, viewing_score


def part1(data) -> int:
    data = [elem.rstrip("\n") for elem in data]
    for i in range(len(data) - 1):
        data[i] = [elem for elem in data[i]]
    return match_patterns(data)[0]


def part2(data) -> int:
    data = [elem.rstrip("\n") for elem in data]
    for i in range(len(data) - 1):
        data[i] = [elem for elem in data[i]]
    return match_patterns(data)[1]

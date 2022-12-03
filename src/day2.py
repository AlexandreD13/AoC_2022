"""
Author:         Alexandre Desfosses
Creation date:  2022-12-02
Documentation:

References:
"""

value: dict = {"A": 1, "B": 2, "C": 3,
               "X": 1, "Y": 2, "Z": 3}

combinations: dict = {"Lose": {"A": "C", "B": "A", "C": "B"},
                      "Win": {"A": "B", "B": "C", "C": "A"},
                      "Draw": {"A": "A", "B": "B", "C": "C"}}


def part1(data: list) -> int:
    score: int = 0
    data: list = "".join(data).replace(" ", "").split("\n")
    for elem in data:
        if elem in ["AY", "BZ", "CX"]:  # Win
            score += value[elem[1]] + 6
        elif elem in ["AX", "BY", "CZ"]:  # Draw
            score += value[elem[1]] + 3
        else:  # Lose
            score += value[elem[1]]
    return score


def part2(data: list) -> int:
    score: int = 0
    data: list = "".join(data).replace(" ", "").split("\n")
    for elem in data:
        if elem[1] == "Z":
            score += value[combinations["Win"][elem[0]]] + 6
        elif elem[1] == "Y":
            score += value[combinations["Draw"][elem[0]]] + 3
        else:
            score += value[combinations["Lose"][elem[0]]]
    return score

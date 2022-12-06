"""
Author:         Alexandre Desfosses
Creation date:  2022-12-05
Documentation:

References:
"""


def clean_initial_positions(initial: list) -> dict:
    dct: dict = {1: "", 2: "",
                 3: "", 4: "",
                 5: "", 6: "",
                 7: "", 8: "",
                 9: ""}
    for line in initial[:-1]:
        for i in range(1, len(line) - 1):
            if i == 1:
                character: str = line[i: i + 1]
            else:
                character: str = line[3 * i + (i - 3): 3 * i + (i - 2)]
            if character not in ["", " "]:
                dct[i] = dct[i] + character
    return dct


def clean_instructions(instructions: list) -> any:
    instructions = [elem.split(" ") for elem in instructions]
    return [[int(elem[1]), int(elem[3]), int(elem[5])] for elem in instructions]


def part1(data) -> str:
    data = [elem.rstrip("\n") for elem in data]
    initial: list = data[0:9]
    instructions: list = data[10:]
    initial: dict = clean_initial_positions(initial)
    instructions = clean_instructions(instructions)
    for elem in instructions:
        temp: str = initial[elem[1]][:elem[0]]
        initial[elem[1]] = initial[elem[1]][elem[0]:]
        for char in temp:
            initial[elem[2]] = char + initial[elem[2]]
    res: str = ""
    for i in range(1, 10):
        res = res + initial[i][0]
    return res


def part2(data) -> str:
    data = [elem.rstrip("\n") for elem in data]
    initial: list = data[0:9]
    instructions: list = data[10:]
    initial: dict = clean_initial_positions(initial)
    instructions = clean_instructions(instructions)
    for elem in instructions:
        temp: str = initial[elem[1]][:elem[0]]
        initial[elem[1]] = initial[elem[1]][elem[0]:]
        initial[elem[2]] = temp + initial[elem[2]]
    res: str = ""
    for i in range(1, 10):
        res = res + initial[i][0]
    return res

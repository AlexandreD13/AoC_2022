"""
Author:         Alexandre Desfosses
Creation date:  2022-12-01
Version:        1.0   ->    Creation of file (Version will only be updated when all days are done)
Documentation:

References:
"""

import day1
import day2
import day3
import day4
import day5
import day6
import day7
import day8
import day9
import day10
import day11
import day12
import day13
import day14
import day15
import day16
import day17
import day18
import day19
import day20
import day21
import day22
import day23
import day24
import day25

from Color import Color
import os
import time


def main():
    for day in range(1, 26):

        # Import data
        input_file: str = "../input/day" + str(day) + ".txt"
        if os.path.exists(input_file):
            with open(input_file, "r") as file:
                data: list = [line for line in file]
        else:
            raise FileExistsError(f"File '{input_file}' does not exist.")

        # Proof of concept for importing functions in a loop
        print(f"\n{Color.GREEN}{Color.BOLD}Day {day}{Color.END}")
        print(f"Filepath :\t\t\t\t{Color.BLUE}'{input_file}'{Color.END}")

        if len(data) > 0:
            print(f"Imported data :\t\t\t{Color.BLUE}{data[0:5]} (...){Color.END}")

            function_calls: list[list] = [[day1.part1, day1.part2],
                                          [day2.part1, day2.part2]]
            # (day3.part1(data), day3.part2(data)),
            # (day4.part1(data), day4.part2(data)),
            # (day5.part1(data), day5.part2(data)),
            # (day6.part1(data), day6.part2(data)),
            # (day7.part1(data), day7.part2(data)),
            # (day8.part1(data), day8.part2(data)),
            # (day9.part1(data), day9.part2(data)),
            # (day10.part1(data), day10.part2(data)),
            # (day11.part1(data), day11.part2(data)),
            # (day12.part1(data), day12.part2(data)),
            # (day13.part1(data), day13.part2(data)),
            # (day14.part1(data), day14.part2(data)),
            # (day15.part1(data), day15.part2(data)),
            # (day16.part1(data), day16.part2(data)),
            # (day17.part1(data), day17.part2(data)),
            # (day18.part1(data), day18.part2(data)),
            # (day19.part1(data), day19.part2(data)),
            # (day20.part1(data), day20.part2(data)),
            # (day21.part1(data), day21.part2(data)),
            # (day22.part1(data), day22.part2(data)),
            # (day23.part1(data), day23.part2(data)),
            # (day24.part1(data), day24.part2(data)),
            # (day25.part1(data), day25.part2(data))]

            part1_result = function_calls[day - 1][0](data)
            print(f"Result of part 1 :\t\t{Color.BLUE}{part1_result}{Color.END}")

            part2_result = function_calls[day - 1][1](data)
            print(f"Result of part 2 :\t\t{Color.BLUE}{part2_result}{Color.END}")

            # Write results to output file
            output_file: str = "../output/day" + str(day) + ".txt"
            output = open(output_file, "w")  # "a" - append / "w" - write
            output.write(f"{part1_result}\n")
            output.write(f"{part2_result}\n")
            output.close()
        else:
            print(f"{Color.RED}No data in corresponding file{Color.END}{Color.END}")


if __name__ == "__main__":
    start_time: float = time.time()

    main()

    end_time: float = time.time()
    time_taken: float = round((end_time - start_time) * 1000, 3)
    print(f"{Color.YELLOW}\nRuntime :\t\t\t\t{time_taken} ms{Color.END}")

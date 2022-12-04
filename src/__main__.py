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

DAILY_BENCHMARK: bool = True
TOTAL_BENCHMARK: bool = not DAILY_BENCHMARK
# TOTAL_BENCHMARK: bool = False

function_calls: list[list] = [[day1.part1, day1.part2], [day2.part1, day2.part2],
                              [day3.part1, day3.part2], [day4.part1, day4.part2],
                              [day5.part1, day5.part2], [day6.part1, day6.part2],
                              [day7.part1, day7.part2], [day8.part1, day8.part2],
                              [day9.part1, day9.part2], [day10.part1, day10.part2],
                              [day11.part1, day11.part2], [day12.part1, day12.part2],
                              [day13.part1, day13.part2], [day14.part1, day14.part2],
                              [day15.part1, day15.part2], [day16.part1, day16.part2],
                              [day17.part1, day17.part2], [day18.part1, day18.part2],
                              [day19.part1, day19.part2], [day20.part1, day20.part2],
                              [day21.part1, day21.part2], [day22.part1, day22.part2],
                              [day23.part1, day23.part2], [day24.part1, day24.part2],
                              [day25.part1, day25.part2]]


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

            if DAILY_BENCHMARK:
                timer1 = []
                for _ in range(0, 1001):
                    start_time1: float = time.time()

                    part1_result = function_calls[day - 1][0](data)
                    part2_result = function_calls[day - 1][1](data)

                    end_time1: float = time.time()
                    time_taken1: float = end_time1 - start_time1
                    timer1.append(time_taken1)
                print(f"Result of part 1 :\t\t{Color.BLUE}{part1_result}{Color.END}")
                print(f"Result of part 2 :\t\t{Color.BLUE}{part2_result}{Color.END}")
                print(f"{Color.YELLOW}\nTotal Runtime :\t\t{round(sum(timer1) * 1000, 5)} ms{Color.END}")
                print(f"{Color.YELLOW}Dayly Average Runtime :\t\t{round(sum(timer1) * 1000 / 1000, 5)} ms{Color.END}")
            else:
                part1_result = function_calls[day - 1][0](data)
                print(f"Result of part 1 :\t\t{Color.BLUE}{part1_result}{Color.END}")

                part2_result = function_calls[day - 1][1](data)
                print(f"Result of part 2 :\t\t{Color.BLUE}{part2_result}{Color.END}")
        else:
            print(f"{Color.RED}No data in corresponding file{Color.END}{Color.END}")


if __name__ == "__main__":
    if TOTAL_BENCHMARK:
        timer2: list = []
        for _ in range(0, 1001):
            start_time2: float = time.time()

            main()

            end_time2: float = time.time()
            time_taken2: float = end_time2 - start_time2
            timer2.append(time_taken2)
        print(f"{Color.YELLOW}\nTotal Runtime :\t\t{round(sum(timer2) * 1000, 5)} ms{Color.END}")
        print(f"{Color.YELLOW}Total Average Runtime :\t\t{round(sum(timer2) * 1000 / 1000, 5)} ms{Color.END}")
    else:
        main()

from typing import List

import common

INPUT = 'input.txt'
# INPUT = 'sample.txt'
lines = common.read_lines(INPUT)


def get_target(num_ones, num_zeros, is_most_common):
    target = '1' if num_ones >= num_zeros else '0'
    if not is_most_common:
        if target == '1':
            target = '0'
        else:
            target = '1'
    return target


def filter_most_least_common(filtered_lines: List[str], is_most_common: bool) -> str:
    i = 0
    while len(filtered_lines) > 1:
        transposed = [list(i) for i in zip(*filtered_lines)]
        print(transposed)
        while i < len(transposed):
            line = transposed[i]
            num_ones = len([x for x in line if x == '1'])
            num_zeros = len(line) - num_ones
            target = get_target(num_ones, num_zeros, is_most_common)
            filtered_lines = [x for x in filtered_lines if x[i] == target]
            if len(filtered_lines) == 1:
                break
            transposed = [list(i) for i in zip(*filtered_lines)]
            i += 1
            print(filtered_lines)
    return filtered_lines[0]


oxygen = int(filter_most_least_common(lines, True), 2)
co2 = int(filter_most_least_common(lines, False), 2)

print(oxygen * co2)

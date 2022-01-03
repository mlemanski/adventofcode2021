from typing import List, Tuple

import common

INPUT = 'input.txt'
# INPUT = 'sample.txt'
LINES = common.read_lines(INPUT)

lowest = []


def get_valid_locations(locations: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    return [loc for loc in locations if 0 <= loc[0] < len(LINES) and 0 <= loc[1] < len(LINES[0])]


for i in range(0, len(LINES)):
    curr_line = list(LINES[i])
    for j in range(0, len(curr_line)):
        above = i-1, j
        right = i, j+1
        below = i+1, j
        left = i, j-1
        neighbors = get_valid_locations([above, right, below, left])
        curr = int(curr_line[j])
        curr_is_lowest = True
        for k in neighbors:
            neighbor = list(LINES[k[0]])[k[1]]
            if int(neighbor) <= curr:
                curr_is_lowest = False
        if curr_is_lowest:
            lowest.append(curr+1)

print(lowest)
print(sum(lowest))

from pprint import pprint
from typing import List, Tuple

import common

# INPUT = 'input.txt'
INPUT = 'sample.txt'
LINES = common.read_lines(INPUT)

GRID = [[]]


def find_max_xy(coordinate_pairs: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> Tuple[int,int]:
    max_x = 0
    max_y = 0
    for (lx,ly), (rx,ry) in coordinate_pairs:
        max_x = max(max_x, max(lx, rx))
        max_y = max(max_y, max(ly, ry))
    return max_x, max_y


def parse_file(lines) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    pairs = []
    for line in lines:
        left, right = line.split(' -> ')
        lx, ly = left.split(',')
        rx, ry = right.split(',')
        pairs.append(((int(lx), int(ly)), (int(rx), int(ry))))
    return pairs


def is_horizontal(left, right):
    return left[1] == right[1]


def is_vertical(left, right):
    return left[0] == right[0]


def is_diagonal(left, right):
    return (left[0] - right[0]) == (left[1] - right[1])


def fill_grid(coordinate_pairs: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> None:
    for left, right in coordinate_pairs:
        if is_horizontal(left, right):
            y = left[1]
            lx = left[0]
            rx = right[0]
            for x in range(min(lx, rx), max(lx, rx)+1):
                GRID[y][x] += 1
        elif is_vertical(left, right):
            x = left[0]
            ly = left[1]
            ry = right[1]
            for y in range(min(ly, ry), max(ly, ry)+1):
                GRID[y][x] += 1
        elif is_diagonal(left, right):
            lx, ly = left
            rx, ry = right
            for x in range(min(lx, rx), max(lx, rx)+1):
                for y in range(min(ly, ry), max(ly, ry)+1):
                    GRID[y][x] += 1


def count_greater_than_one(grid: List[List[int]]) -> int:
    count = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] > 1:
                count += 1
    return count


if __name__ == '__main__':
    coordinate_pairs = parse_file(LINES)
    max_x, max_y = find_max_xy(coordinate_pairs)
    GRID = [[0]*(max_x+1) for _ in range(max_y+1)]
    fill_grid(coordinate_pairs)
    pprint(GRID)
    print(count_greater_than_one(GRID))

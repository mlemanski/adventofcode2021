from typing import List

import common

INPUT = 'input.txt'
# INPUT = 'sample.txt'
LINES = common.read_lines(INPUT)

ROWS = 5
COLUMNS = 5


class Board:
    def __init__(self, board_lines: str):
        self.values = board_lines.split()
        self.chosen = [False]*(ROWS*COLUMNS)

    def get_row(self, i: int) -> List[bool]:
        return self.chosen[i * ROWS:(i + 1) * ROWS]

    def get_column(self, j: int) -> List[bool]:
        return self.chosen[j::COLUMNS]

    def is_winner(self):
        for i in range(0, ROWS):
            row = self.get_row(i)
            if all(row):
                return True
        for i in range(0, COLUMNS):
            col = self.get_column(i)
            if all(col):
                return True
        return False

    def updated_selected(self, val: str):
        for i in range(0, ROWS*COLUMNS):
            if self.values[i] == val:
                self.chosen[i] = True

    def unmarked_sum(self):
        total = 0
        for i, val in enumerate(self.chosen):
            if not val:
                total += int(self.values[i])
        return total


    def print(self):
        result1 = ''
        result2 = ''
        total_result = f'{self.is_winner()}\n'
        for i in range(0, ROWS*COLUMNS):
            result1 += f'{self.values[i]} '.rjust(3, ' ')
            result2 += f'{self.chosen[i]} '
            if i > 1 and ((i+1) % COLUMNS == 0):
                total_result += f'{result1} {result2}\n'
                result1 = ''
                result2 = ''
        print(total_result)


def parse_boards(lines: List[str]) -> List[Board]:
    parsed_boards = []
    i = 0
    current_board = ''
    for line in lines:
        if not line:
            continue

        current_board += f'{line} '
        i += 1

        if i % COLUMNS == 0:
            board = Board(current_board)
            parsed_boards.append(board)
            current_board = ''

    return parsed_boards


if __name__ == '__main__':
    first_line = LINES[0]
    number_sequence = first_line.split(',')

    boards = parse_boards(LINES[1:])

    last_winner = None
    last_winner_val = None

    for val in number_sequence:
        i = len(boards) - 1
        while i > 0:
            board = boards[i]
            board.updated_selected(val)
            if board.is_winner():
                last_winner = board
                last_winner_val = int(val)
                boards.pop(i)
            i -= 1

    if last_winner:
        unmarked_sum = last_winner.unmarked_sum()
        print(unmarked_sum * int(last_winner_val))
        last_winner.print()
    else:
        print("?!")

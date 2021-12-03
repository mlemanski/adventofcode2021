from typing import List


def read_input(filename: str) -> List[str]:
    with open(filename) as f:
        return [x.rstrip() for x in f.readlines()]

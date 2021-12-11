
import common

INPUT = 'input.txt'
# INPUT = 'sample.txt'

with open(INPUT) as f:
    LINE = f.readline().rstrip()

positions = [int(_) for _ in LINE.split(',')]
costs = []
min_cost = None

for i in range(0, len(positions)):
    curr_cost = 0
    for j in positions:
        curr_cost += abs(j - i)
    min_cost = curr_cost if not min_cost else min(min_cost, curr_cost)

print(min_cost)

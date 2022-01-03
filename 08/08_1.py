
import common

INPUT = 'input.txt'
# INPUT = 'sample.txt'
LINES = common.read_lines(INPUT)

unique_segment_lengths = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
}

total = 0

for line in LINES:
    left, right = line.split(' | ')
    left_vals = left.split()
    right_vals = right.split()

    for x in right_vals:
        if len(x) in unique_segment_lengths:
            total += 1

print(total)

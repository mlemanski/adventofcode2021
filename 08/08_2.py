
import common

# INPUT = 'input.txt'
INPUT = 'sample.txt'
LINES = common.read_lines(INPUT)

# 0 -> 6
# 1 -> 2
# 2 -> 5
# 3 -> 5
# 4 -> 4
# 5 -> 5
# 6 -> 6
# 7 -> 3
# 8 -> 7
# 9 -> 6
#
# 1 then 7 reveals a (len 2, 3)
# 3 then 4 reveals b
# 0 then 8 reveals c (len
# 9 then 8 reveals e, 5 then 6 reveals e
# 2 then 3 reveals e, f
# 6 then 9 reveals c, e
# b
# d
# f

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

    remapping_chars = {x: None for x in 'abcdefg'}
    per_letter_map = {x: set() for x in range(0,10)} # 1 -> ab, 2 -> acdef, 7 -> abc, etc

    left_vals_by_len = sorted(left_vals, key=len)

    # uniques
    for x in left_vals_by_len:
        if len(x) == 2:
            per_letter_map[1] = set(list(x))
        elif len(x) == 3:
            per_letter_map[7] = set(list(x))
            diff_1_7 = list(per_letter_map[7] - per_letter_map[1])
            remapping_chars[diff_1_7[0]] = 'a'

print(total)

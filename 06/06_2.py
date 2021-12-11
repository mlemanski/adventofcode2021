#
# import common
#
# # INPUT = 'input.txt'
# INPUT = 'sample.txt'
#
# with open(INPUT) as f:
#     LINE = f.readline().rstrip()
#
# ages = [int(_) for _ in LINE.split(',')]
#
# for generation in range(0, 256):
#     num_new_fish = 0
#     for i, age in enumerate(ages):
#         if age == 0:
#             num_new_fish += 1
#             ages[i] = 6
#         else:
#             ages[i] -= 1
#     ages.extend([8]*num_new_fish)
#
# print(len(ages))

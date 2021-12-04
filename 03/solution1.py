import common

lines = common.read_input('input.txt')
transposed = [list(i) for i in zip(*lines)]

frequent_bits = ''
infrequent_bits = ''

for line in transposed:
    num_ones = len([x for x in line if x == '1'])
    num_zeros = len(line) - num_ones
    if num_ones > num_zeros:
        frequent_bits += '1'
        infrequent_bits += '0'
    else:
        frequent_bits += '0'
        infrequent_bits += '1'

gamma = int(frequent_bits, 2)
epsilon = int(infrequent_bits, 2)
print(f'{gamma * epsilon} -> {bin(gamma * epsilon)}')

with open('input.txt') as f:
    lines = [x.rstrip() for x in f.readlines()]

aim = 0
xz = [0, 0]

for x in lines:
    cmd, val = x.split()
    val = int(val)

    if cmd == 'forward':
        xz = xz[0] + val, xz[1] + aim*val
    elif cmd == 'down':
        aim += val
    elif cmd == 'up':
        aim -= val

print(xz[0]*xz[1])


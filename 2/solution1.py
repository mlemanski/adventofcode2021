with open('input.txt') as f:
    lines = [x.rstrip() for x in f.readlines()]

xz = [0, 0]

for x in lines:
    cmd, val = x.split()
    val = int(val)

    if cmd == 'forward':
        xz[0] += val
    elif cmd == 'down':
        xz[1] += val
    elif cmd == 'up':
        xz[1] -= val

print(xz[0]*xz[1])


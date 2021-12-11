with open('input.txt') as f:
    lines = [int(x) for x in f.readlines() if x[:-1]]

count = 0
window = lines[0:3]
for x in lines[3:]:
    next_window = [window[1], window[2], x]
    if sum(next_window) > sum(window):
        count += 1
    window = next_window

print(count)


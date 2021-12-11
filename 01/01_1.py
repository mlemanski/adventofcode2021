with open('input.txt') as f:
    lines = f.readlines()
    count = 0
    prev_val = None

    for x in lines:
        line_val = x[:-1]
        if line_val:
            line_int = int(line_val)
            if prev_val and line_int > prev_val:
                count += 1
            prev_val = line_int

    print(count)

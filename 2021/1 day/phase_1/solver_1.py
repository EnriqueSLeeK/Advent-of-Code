with open("input", "r") as f:
    tot = 0
    cmp_first = int(f.readline())
    for line in f:
        cmp_sec = int(line)
        if (cmp_first < cmp_sec):
            tot += 1
        cmp_first = cmp_sec
    print(tot)

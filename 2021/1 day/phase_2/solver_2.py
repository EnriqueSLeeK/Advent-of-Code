def transfer(src, dst, times):
    for k in range(times):
        dst.append(src.pop(0))

with open("input", "r") as f:
    group = [[], [], [], []]
    tot = 0
    cyle_step = 0

    for line in f:
        cyle_step += 1
        val = int(line)
        if (len(group[0]) < 3):
            group[0].append(val)
        if (cyle_step > 1 and len(group[1]) < 3):
            group[1].append(val)
        if (cyle_step > 2 and len(group[2]) < 2):
            group[2].append(val)
        if (cyle_step > 3):
            group[3].append(val)
        if (cyle_step % 4 == 0):
            if (sum(group[0]) < sum(group[1])):
                tot += 1
            cyle_step = 3
            group[0] = []
            transfer(group[1], group[0], 3)
            group[1] = []
            transfer(group[2], group[1], 2)
            group[2] = []
            transfer(group[3], group[2], 1)
            group[3] = []
    print(tot)

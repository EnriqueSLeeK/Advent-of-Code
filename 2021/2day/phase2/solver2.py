with open("input", "r") as f:
    coord = [0, 0]
    aim = 0
    for line in f:
        cmd, steps = line.split()
        steps = int(steps)
        if (cmd == "forward"):
            coord[0] += steps
            coord[1] += aim * steps
        elif (cmd == "up"):
            aim -= steps
        elif (cmd == "down"):
            aim += steps
    print(coord[0] * coord[1])

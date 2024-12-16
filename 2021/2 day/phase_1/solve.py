with open("input", "r") as f:
    coord = [0, 0]
    for line in f:
        cmd, steps = line.split()
        steps = int(steps)
        if (cmd == "forward"):
            coord[0] += steps
        elif (cmd == "up"):
            coord[1] -= steps
        elif (cmd == "down"):
            coord[1] += steps
    print(coord[0] * coord[1])

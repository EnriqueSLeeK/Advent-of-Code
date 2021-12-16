with open("input", "r") as f:
    lines = [[int(num) for num in list(line.strip())] for line in f]

x_max = len(lines[0])
y_max = len(lines)

distance = [[-1] * (x_max) for k in range(y_max)]
distance[0][0] = lines[0][0]

def check_index(index, max_index):
    if (index > -1 and index < max_index):
        return (True)
    return (False)

for y in range(y_max):
    for x in range(x_max):

        if (check_index(y + 1, y_max)):
            tentative_disty = distance[y][x] + lines[y + 1][x]

            if (distance[y + 1][x] == -1):
                distance[y + 1][x] =  tentative_disty

            else:
                distance[y + 1][x] = tentative_disty if tentative_disty < distance[y + 1][x] else distance[y + 1][x]

        if (check_index(x + 1, x_max)):
            tentative_distx = distance[y][x] + lines[y][x + 1]

            if (distance[y][x + 1] == -1):
                distance[y][x + 1] = tentative_distx

            else:
                distance[y][x + 1] = tentative_distx if tentative_distx < distance[y][x + 1] else distance[y][x + 1]

print(distance[-1][-1] - distance[0][0])

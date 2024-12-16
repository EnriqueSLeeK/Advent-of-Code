with open("input", "r") as f:
    lines = [[int(num) for num in list(line.strip())] for line in f]

x_max = len(lines[0])
y_max = len(lines) + 1

def danger_rising(n):
    if (n < 9):
        return (n + 1)
    return (1)

def grid_expansion():
    for index in range(y_max - 1):
        for n in range(0, 4):
            lines[index] = lines[index] + list(map(danger_rising, lines[index][x_max * n: x_max * (n + 1)]))

grid_expansion()
x_max *= 5

distance = [[-1] * (x_max) for k in range(y_max)]
distance[0][0] = lines[0][0]
adjust = lines[0][0]

def check_index(index, max_index):
    if (index > -1 and index < max_index):
        return (True)
    return (False)

def generate_next_segment():
    lines[0] = lines[-1]
    lines.pop(-1)
    for index in range(1, y_max - 1):
        lines[index] = list(map(danger_rising, lines[index]))

def distance_reset():
    distance[0] = distance[-1].copy()
    for index in range(1, y_max):
        distance[index] = [-1] * (x_max) 

def shortest_path():
    y = 0
    while (y < y_max - 1):
        x = 0
        while(x < x_max):

            if (check_index(y - 1, y_max)):

                tentative_disty = distance[y][x] + lines[y - 1][x]
                if (distance[y - 1][x] == -1):
                    distance[y - 1][x] =  tentative_disty
                else:
                    if (tentative_disty < distance[y - 1][x]):
                        distance[y - 1][x] = tentative_disty
                        y -= 2
                        break

            if (check_index(x - 1, x_max)):

                tentative_distx = distance[y][x] + lines[y][x - 1]
                if (distance[y][x - 1] == -1):
                    distance[y][x - 1] = tentative_distx
                else:
                    if (tentative_distx < distance[y][x - 1]):
                        distance[y][x - 1] = tentative_distx
                        x -= 1
                        continue

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

            x += 1
        y += 1

for k in range(5):
    lines.append(list(map(danger_rising, lines[0])))
    shortest_path()
    generate_next_segment()
    if (k != 4):
        distance_reset()

print(distance[y_max - 2][x_max - 1] - adjust)

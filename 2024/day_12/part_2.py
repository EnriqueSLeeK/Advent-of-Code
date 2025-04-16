from collections import defaultdict, deque

garden_map = []

# with open('input.txt', 'r') as f:
# with open('test', 'r') as f:
with open('a', 'r') as f:
    for line in f:
        garden_map.append(list(line.strip()))

visited = set()

sides = 0
area = 0

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

y_max = len(garden_map)
x_max = len(garden_map[0])

def check_valid(y, x):
    if (y < 0 or x < 0) or (y >= y_max or x >= x_max):
        return False
    return True

def get_dimesion(y, x, region_identifier, visited_cell):

    global perimeter, area

    coord = (y, x)

    if coord in visited:
        return

    visited.add(coord)
    visited_cell.append(coord)
    area += 1
  
    for dir in direction:
        y_next = y + dir[0]
        x_next = x + dir[1]

        if check_valid(y_next, x_next) and garden_map[y_next][x_next] == region_identifier:
            get_dimesion(y_next, x_next, region_identifier, visited_cell.copy())
            visited_cell.append((y_next, x_next))
        else:
            perimeter += 1

total = 0
for y in range(y_max):
    for x in range(x_max):
        if (y, x) not in visited:
            get_dimesion(y, x, garden_map[y][x], [])
            total += sides * area
            perimeter, area = 0, 0

print(total)

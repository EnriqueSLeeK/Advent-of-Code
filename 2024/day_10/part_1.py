
terrain_map = []
# with open('input.txt', 'r') as f:
with open('test', 'r') as f:
# with open('a', 'r') as f:
    for line in f:
        row = []
        for c in list(line.strip()):
            if c == '.':
                row.append(10)
            else:
                row.append(int(c))
        terrain_map.append(row)
        # terrain_map.append(list(map(int, line.strip())))

def find_start():
    start = []
    for y in range(max_y):
        for x in range(max_x):
            if terrain_map[y][x] == 0:
                start.append((y, x))
    return start

def check_if_valid(y, x):
    if (y < 0 or x < 0) or (y >= max_y or x >=  max_x):
        return False
    return True


def explore(terrain_map, y, x, visited, next_level = 1):

    global nine_count
    if next_level == 10:
        nine.add((y, x))

    visited.add((y, x))

    for y_step, x_step in direction:
        y_next = y + y_step
        x_next = x + x_step

        if check_if_valid(y_next, x_next):

            if terrain_map[y_next][x_next] == next_level:

                # print(f"({y_next}, {x_next})", terrain_map[y_next][x_next])
                explore(terrain_map,
                        y_next, x_next,
                        visited.copy(), next_level + 1)

            visited.add((y_next, x_next))

nine_count = 0
max_x, max_y = len(terrain_map[0]), len(terrain_map)
direction = [(1, 0), (0, 1), (0, -1), (-1, 0)]
start_point = find_start()
for start in start_point:
    nine = set()
    explore(terrain_map,
              start[0],
              start[1],
              set(),
              1)
    nine_count += len(nine)
    nine = set()

print(nine_count)
# print(terrain_map)


from math import sin, cos, pi

t_map = None

with open('input.txt', 'r') as f:
# with open('test', 'r') as f:
    t_map = f.read().strip().split('\n')

visited = set()
max_x = len(t_map[0])
max_y = len(t_map)
count_cycle = 0

def calculate_direction(multiplier = 1):
    multiplier = (multiplier + 1) % 4
    radians = pi * multiplier * 0.5
    return (multiplier,
                tuple(map(int , [sin(radians) * -1, cos(radians)])))

def sum_tuples(t_a, t_b):
    return tuple(a + b for a, b in zip(t_a, t_b))

def check_bound(curr_coord):
    return curr_coord[0] >= max_y or curr_coord[1] >= max_x or \
            curr_coord[0] < 0 or curr_coord[1] < 0

def find_guard():
    y_index = -1
    x_index = -1
    for y, line in enumerate(t_map):
        if '^' in line:
            y_index = y
            x_index = line.index('^')
            break
    return (y_index, x_index)

def check_obstacle(obstacle, new_coord):
    if t_map[new_coord[1]][new_coord[0]] == '#' \
        or new_coord == obstacle:
        return True
    return False

def step(coord, obstacle, mult, direction):
    new_coord = sum_tuples(coord, direction)
    multiplicative = mult
    direction_new = direction

    if check_bound(new_coord):
        return (None, None, None)

    while check_obstacle(obstacle, new_coord):
        multiplicative, direction_new = calculate_direction(multiplicative)
        new_coord = sum_tuples(coord, direction_new)

    return (direction_new, multiplicative, new_coord)

def explore(x, y, obstacle):

    global count_cycle
    mult_h, direction_hare = calculate_direction()
    mult_t, direction_tortoise = calculate_direction()

    curr_coord_tortoise = (x, y)
    curr_coord_hare = (x, y)
    encounter = 0
    while True:

        # Hare block ===================
        direction_hare, mult_h, curr_coord_hare = step(curr_coord_hare,
                               obstacle,
                               mult_h,
                               direction_hare)
        if direction_hare is None:
            break

        direction_hare, mult_h, curr_coord_hare = step(curr_coord_hare,
                               obstacle,
                               mult_h,
                               direction_hare)
        if direction_hare is None:
            break
        # Hare block ===================

        # Tortoise block ===============
        direction_tortoise, mult_t, curr_coord_tortoise = step(curr_coord_tortoise,
                                   obstacle,
                                   mult_t,
                                   direction_tortoise)
        if direction_tortoise is None:
            break
        # Tortoise block ===============

        if curr_coord_hare == curr_coord_tortoise:
            encounter += 1

        if encounter >= 3:
            count_cycle += 1
            break

def get_path(x, y, obstacle):

    global visited
    mult, direction = calculate_direction()

    curr_coord = (x, y)

    visited.add(curr_coord)
    while True:

        direction, mult, curr_coord = step(curr_coord, None, mult, direction)
        if direction is None:
            break
        visited.add(curr_coord)

guard_index = find_guard()
visited.add(guard_index)

get_path(guard_index[1], guard_index[0], None)

for v in visited:
    if t_map[v[1]][v[0]] != '^':
        explore(guard_index[1], guard_index[0], v)

print(count_cycle)

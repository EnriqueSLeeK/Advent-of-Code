
from collections import defaultdict

antenna_map = []

with open("input.txt", "r") as f:
# with open("test", "r") as f:
# with open("a", "r") as f:
    for line in f:
        antenna_map.append(list(line.strip()))

def find_antenna(antenna_map):

    antenna_local =  defaultdict(list)

    for i in range(len(antenna_map)):
        for j in range(len(antenna_map[0])):
            if antenna_map[i][j] != '.':
                antenna_local[antenna_map[i][j]].append((i, j))
    return antenna_local

def sum_tuple(tuple_one, tuple_two):
    return tuple([a + b for a, b in zip(tuple_one, tuple_two)])

def sub_tuple(tuple_one, tuple_two):
    return tuple([a - b for a, b in zip(tuple_one, tuple_two)])

def get_front_and_back(antenna, diff):

    front = sum_tuple(antenna, diff)
    back = sub_tuple(antenna, diff)

    return [front, back]


def check_free(coord, antenna):

    if ((coord[1] >= max_x or coord[0] >= max_y)
        or (coord[1] < 0 or coord[0] < 0))\
        or antenna == coord:
        return False
    return True

def count_antinodes(antenna_one, antenna_two):
    res = []

    diff = sub_tuple(antenna_one, antenna_two)
    f_one, b_one = get_front_and_back(antenna_one, diff)
    f_two, b_two = get_front_and_back(antenna_two, diff)

    if check_free(f_one, antenna_two):
        res.append(f_one)
    if check_free(b_one, antenna_two):
        res.append(b_one)

    if check_free(f_two, antenna_one):
        res.append(f_two)
    if check_free(b_two, antenna_one):
        res.append(b_two)

    return res

max_y = len(antenna_map)
max_x = len(antenna_map[0])
antinodes = set()

antenna_local = find_antenna(antenna_map)

for k in antenna_local:
    antennas = antenna_local[k]
    antenna_count = len(antennas)
    for i in range(antenna_count):
        for j in range(i + 1, antenna_count):
            antinodes.update(count_antinodes(antennas[i], antennas[j]))

# print(antinodes)
print(len(antinodes))

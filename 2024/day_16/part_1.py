
from heapq import heappop, heappush

from collections import defaultdict

maze = []

with open('input', 'r') as f:
# with open('test', 'r') as f:
    for line in f:
        maze.append(line.strip())

# (y, x)
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

clockwise = {
    (0, 1): direction[1],
    (1, 0): direction[2],
    (0, -1): direction[3],
    (-1, 0): direction[0]
}

anticlockwise = {
    (0, 1): direction[-1],
    (-1, 0): direction[-2],
    (0, -1): direction[-3],
    (1, 0): direction[0]
}

# Returns -> (y, x)
def find_point(maze, symbol):

    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == symbol:
                return (y, x)

    return (-1, -1)


def explore_a_star(maze, start_point, end_point):

    visiting = []
    heappush(visiting, (0, start_point, direction[0]))

    visited = defaultdict(lambda: float("inf"))
    visited[(start_point, direction[0])] = 0

    while visiting:
        cost, coord, dir = heappop(visiting)

        if coord == end_point:
            return cost

        new_coord = (coord[0] + dir[0], coord[1] + dir[1])

        if maze[new_coord[0]][new_coord[1]] != '#':
            new_cost = cost + 1
            if new_cost < visited[(new_coord, dir)]:
                visited[(new_coord, dir)] = new_cost
                heappush(visiting, (new_cost, new_coord, dir))

        new_cost = cost + 1000


        new_dir = clockwise[dir]
        if new_cost < visited[(coord, new_dir)]:
            visited[(coord, new_dir)] = new_cost
            heappush(visiting, (new_cost, coord, new_dir))

        new_dir = anticlockwise[dir]
        if new_cost < visited[(coord, new_dir)]:
            visited[(coord, new_dir)] = new_cost
            heappush(visiting, (new_cost, coord, new_dir))

    return float('inf')


start = find_point(maze, 'S')
end = find_point(maze, 'E')

print(explore_a_star(maze, start, end))

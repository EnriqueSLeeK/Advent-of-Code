
points = []
velocity = []

steps = 100

dimension = (11, 7)
# dimension = [101, 103]

# with open('input', 'r') as f:
with open('test', 'r') as f:
    for line in f:
        splitted = line.split()
        points.append(list(map(int,splitted[0][2:].split(','))))
        velocity.append(tuple(map(int, splitted[1][2:].split(','))))

for _ in range(steps):
    for i in range(len(points)):
        points[i][0] = (points[i][0] + velocity[i][0]) % dimension[0]
        points[i][1] = (points[i][1] + velocity[i][1]) % dimension[1]

middle_cross = (dimension[0] // 2, dimension[1] // 2)
quadrants_x = [(0, middle_cross[0]), (middle_cross[0] + 1, dimension[0])]
quadrants_y = [(0, middle_cross[1]), (middle_cross[1] + 1, dimension[1])]

def quadrant_robot_count(x_dim, y_dim):

    count = 0
    for p in points:
        # print(p, x_dim, y_dim)
        # print(f"{x_dim[0]} >= {p[0]}")
        # print(f"{x_dim[1]} < {p[0]}")
        # print(x_dim[1] < p[0])

        if ((x_dim[0] <= p[0] and x_dim[1] > p[0]) and
            (y_dim[0] <= p[1] and y_dim[1] > p[1])):
            count += 1

    return count

res = 1

for x_dim in quadrants_x:
    for y_dim in quadrants_y:
        res *= quadrant_robot_count(x_dim, y_dim)

print(res)



points = []
velocity = []

dimension = [101, 103]

def print_board(points, i):
    print(f"- {i}")
    board = [list('.' * dimension[0]) for _ in range(dimension[1])]
    for p in points:
        board[p[1]][p[0]] = '#'

    for line in board:
        print("".join(line))


with open('input', 'r') as f:
    for line in f:
        splitted = line.split()
        points.append(list(map(int,splitted[0][2:].split(','))))
        velocity.append(tuple(map(int, splitted[1][2:].split(','))))

# Deep copy
points_hare = [[k for k in p] for p in points]


k = 0
cycle = []
while True:
    print_board(points, k)
    for i in range(len(points)):
        points[i][0] = (points[i][0] + velocity[i][0]) % dimension[0]
        points[i][1] = (points[i][1] + velocity[i][1]) % dimension[1]
        points_hare[i][0] = (points_hare[i][0] + (velocity[i][0] * 2)) % dimension[0]
        points_hare[i][1] = (points_hare[i][1] + (velocity[i][1] * 2)) % dimension[1]

    k += 1
    if points == points_hare:
        break




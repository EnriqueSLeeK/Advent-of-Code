with open("input", "r") as f:
    lines = f.readlines()

lines = [[int(digit) for digit in list(line.replace('\n', ''))] 
        for line in lines]

y_max = len(lines)
x_max = len(lines[0])

visited = []

flash_point = 0

def check_index(y, x):
    if ( (x > -1 and x < x_max) and
         (y > -1 and y < y_max) ):
        return (True)
    return (False)

def flash_boom(y, x):

    flash = [[-1, 0], [1, 0], [0, -1], [0, 1],
            [1, 1], [-1, -1], [-1, 1], [1, -1]]
    point = [y, x]

    if (point not in visited):
        visited.append(point)
        for look_at in flash:

            if (check_index(y + look_at[0], x + look_at[1])):
                lines[y + look_at[0]][x + look_at[1]] += 1
                point_2 = [y + look_at[0], x + look_at[1]]

                if (lines[y + look_at[0]][x + look_at[1]] > 9 and
                    point_2 not in visited):
                    flash_boom(y + look_at[0], x + look_at[1])

def increment(y, x):
    lines[y][x] += 1
    if (lines[y][x] > 9):
        flash_boom(y, x)

def exhausted_squid():
    global flash_point
    for y in range(y_max):
        for x in range(x_max):
            if (lines[y][x] > 9):
                flash_point += 1
                lines[y][x] = 0

for step in range(100):
    for y in range(y_max):
        for x in range(x_max):
            increment(y, x)
    exhausted_squid()
    visited = []

print(flash_point)

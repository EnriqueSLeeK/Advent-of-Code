with open("input", "r") as f:
    lines = [[int(num) 
            for num in line.replace(' -> ', ',').split(',')] 
            for line in f.readlines()]

x1 = [line[0] for line in lines]
y1 = [line[1] for line in lines]

x2 = [line[2] for line in lines]
y2 = [line[3] for line in lines]

max_x1 = max(x1)
max_x2 = max(x2)

max_y1 = max(y1)
max_y2 = max(y2)

maximum_x = 1 + (max_x1 if max_x1 > max_x2 else max_x2)
maximum_y = 1 + (max_y1 if max_y1 > max_y2 else max_y2)

field = [0] * ((maximum_x + 1) * (maximum_y + 1))

def zip_and_sort(c1, c2):
    coord = [c1, c2]
    coord.sort()
    return (coord)

def add(arr, startx, starty, endx, endy):

    if (startx == endx):
        stepy = 1 if starty < endy else -1
        for y in range(starty, endy + stepy, stepy):
            coord = (maximum_x * y) + startx
            arr[coord] += 1

    elif (starty == endy):
        stepx = 1 if startx < endx else -1
        for x in range(startx, endx + stepx, stepx):
            coord = (maximum_x * starty) + x
            arr[coord] += 1
    else:
        stepx = 1 if startx < endx else -1
        stepy = 1 if starty < endy else -1
        for x, y in zip(range(startx, endx + stepx, stepx),
                 range(starty, endy + stepy, stepy)):
            coord = (maximum_x * y) + x
            arr[coord] += 1

for x, y, x_2, y_2 in zip(x1, y1, x2, y2):
    add(field, x, y, x_2, y_2)

tot = 0
for k in field:
    if (k > 1):
        tot += 1

print(tot)

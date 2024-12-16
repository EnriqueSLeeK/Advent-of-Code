
button_a = []
button_b = []
prize_coord = []

with open('input.txt', 'r') as f:
# with open('test', 'r') as f:
    for line in f:
        if line == '\n':
            continue

        label = line[line.index(':') - 1]
        label_clean = line[line.index(':') + 2:].strip()
        split_coord = label_clean.split(', ')

        if label == 'A':
            button_a.append((int(split_coord[0][2:]), int(split_coord[1][2:])))
        elif label == 'B':
            button_b.append((int(split_coord[0][2:]), int(split_coord[1][2:])))
        else:
            # Part 1
            # prize_coord.append((int(split_coord[0][2:]),
            #                    int(split_coord[1][2:])))

            # Part 2
            prize_coord.append((10000000000000 + int(split_coord[0][2:]),
                               10000000000000 + int(split_coord[1][2:])))

def calculate_b_button_press(a, b, prize):
    return ((a[0] * prize[1]) - (a[1] * prize[0])) // ((a[0] * b[1]) - (a[1] * b[0]))

def calculate_a_button_press(a, b, prize, b_press):
    return (prize[0] - (b[0] * b_press)) // a[0]

point = 0

def calculate_final_coord(a, b, button_a_press, button_b_press):
    return (a[0] * button_a_press + b[0] * button_b_press,
            a[1] * button_a_press + b[1] * button_b_press)

for a, b, prize in zip(button_a, button_b, prize_coord):
    button_b_press = calculate_b_button_press(a, b, prize)
    button_a_press = calculate_a_button_press(a, b, prize, button_b_press)

    if (calculate_final_coord(a, b, button_a_press, button_b_press) == prize):
        point += button_a_press * 3 + button_b_press

print(point)

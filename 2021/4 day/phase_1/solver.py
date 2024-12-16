draw_nums = []
table_list = []

with open("input", "r") as f:
    draw_nums = [int(num) for num in f.readline().split(",")]
    for line in f:
        if (line == "\n"):
            continue
        else:
            table_list.append([int(num) for num in line.split()])

def check_win(table, id):
    for index in range(5):
        #horizontal check
        hit = 0
        line = table[(id * 5) + index]
        for k in line:
            if (k in drawn):
                hit += 1
        if (hit == 5):
            return (True)

    for h_index in range(5):
        #Vertical check
        hit_v = 0
        for v_index in range(5):
            if (table[(id * 5) + v_index]
                [h_index] in drawn):
                hit_v += 1
        if (hit_v == 5):
            return (True)
    return (False)

recent_draw = -1
winner = -1
sum = 0
drawn = []

for num in draw_nums:
    draw = draw_nums.pop(0)
    recent_draw = draw
    drawn.append(draw)
    for id in range(len(table_list) // 5):
        if (check_win(table_list, id)):
            winner = id
            break
    if (winner > -1):
        break

for k in range(5):
    line = table_list[(winner * 5) + k]
    for num in line:
        if (num not in drawn):
            sum += num

print(sum * recent_draw)

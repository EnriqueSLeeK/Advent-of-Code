with open("input", "r") as f:
    lines = [data for data in f.read().split("\n\n")]

coordinates = [[int(num) for num in pair.split(",")]
                             for pair in lines[0].split("\n")]

folding_op = [[fold.replace("fold along ", "") for fold in folds.split("=")] 
                                                   for folds in lines[1].split("\n")]
folding_op.pop(-1)

def apply_fold(op, mode):
    folding_index = int(op[1])
    for pair in coordinates:
        if (folding_index < pair[mode]):
            diff = pair[mode] - folding_index
            pair[mode] = folding_index - diff

def folding(op):
    if (op[0] == 'y'):
        apply_fold(op, 1)
    elif (op[0] == 'x'):
        apply_fold(op, 0)
    else:
        return

def show_code():
    for y in range(y_max + 1):
        for x in range(x_max + 1):
            point = [x, y]
            if (point in coordinates):
                print("#", end = "")
            else:
                print(" ", end = "")
        print()

for op in folding_op:
    folding(op)

x_max = max([num[0] for num in coordinates])
y_max = max([num[1] for num in coordinates])

show_code()


import os
import time

robot_maze = []
moves = []

# (y, x)
movement = {
    '>' : (0, 1),
    '<' : (0, -1),
    '^' : (-1, 0),
    'v' : (1, 0)
}

# with open('input', 'r') as f:
with open('test', 'r') as f:
    maze = True
    for line in f:
        if line == '\n':
            maze = False
            continue

        if maze:
            robot_maze.append(list(line.strip()))
        else:
            moves.append(line.strip())

x_max = len(robot_maze[0])
y_max = len(robot_maze)

def clear_screen():
    os.system('clear')

def print_board(board):
    print()
    print('-' * ((x_max // 2) - (len('Board') // 2)) + 'Board')
    for line in board:
        print(''.join(line), flush=True)

def find_robot(board):
    for y in range(y_max):
        for x in range(x_max):
            if board[y][x] == '@':
                return [y, x]

def step(board, y, x, direction):
    global robot

    x_next = x + direction[1]
    y_next = y + direction[0]
    if board[y_next][x_next] == '#':
        return

    elif board[y_next][x_next] == 'O':
        step(board, y_next, x_next, direction)

    if board[y_next][x_next] == '.':
        board[y][x], board[y_next][x_next] = board[y_next][x_next], board[y][x]
        robot = [y_next, x_next]

def calculate_points(board):
    total = 0
    for y in range(y_max):
        for x in range(x_max):
            if board[y][x] == 'O':
                total += 100 * y + x
    return total

clear_screen()
print_board(robot_maze)
robot = find_robot(robot_maze)

for list_move in moves:
    for action in list_move:
        step(robot_maze, robot[0], robot[1], movement[action])
        # clear_screen()
        # print_board(robot_maze)
        # print(f"-> action: {action}")
        # print(f"robot coordinate: {robot}")
        # time.sleep(0.5)

print(calculate_points(robot_maze))

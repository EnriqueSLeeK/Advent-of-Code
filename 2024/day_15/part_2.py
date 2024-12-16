
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

expansion = {
    '@': '@.',
    'O': '[]',
    '.': '..',
    '#': '##'
}

with open('input', 'r') as f:
# with open('test', 'r') as f:
    maze = True
    for line in f:
        if line == '\n':
            maze = False
            continue

        if maze:
            maze_row = []
            for c in line.strip():
                maze_row.extend(expansion[c])
            robot_maze.append(maze_row)
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

def check_move(board, y, x, direction):

    y_next = y + direction[0]
    x_next = x + direction[1]

    if board[y_next][x_next] == '#':
        return False

    if board[y_next][x_next] == '.':
        return True

    if movement['>'] == direction or movement['<'] == direction:
        return check_move(board, y_next, x_next, direction)
    else:
        if board[y_next][x_next] == '[':
            return (check_move(board, y_next, x_next + 1, direction) and
                check_move(board, y_next, x_next, direction))

        if board[y_next][x_next] == ']':
            return (check_move(board, y_next, x_next - 1, direction) and
                check_move(board, y_next, x_next, direction))

    return False

def step(board, y, x, direction):
    global robot

    x_next = x + direction[1]
    y_next = y + direction[0]

    if not check_move(board, y, x, direction):
        return False

    if board[y_next][x_next] == '[':
        step(board, y_next, x_next + 1, direction)
        step(board, y_next, x_next, direction)

    if board[y_next][x_next] == ']':
        step(board, y_next, x_next - 1, direction)
        step(board, y_next, x_next, direction)

    if board[y_next][x_next] == '.':
        board[y][x], board[y_next][x_next] = board[y_next][x_next], board[y][x]
        robot = [y_next, x_next]

def calculate_points(board):
    total = 0
    for y in range(y_max):
        for x in range(x_max):
            if board[y][x] == '[':
                total += 100 * y + x
    return total

# clear_screen()
# print_board(robot_maze)
# print(moves)
robot = find_robot(robot_maze)

for list_move in moves:
    for action in list_move:
        if check_move(robot_maze, robot[0], robot[1], movement[action]):
            step(robot_maze, robot[0], robot[1], movement[action])
            # print_board(robot_maze)
            # print(f"-> action: {action}")
            # print(f"robot coordinate: {robot}")
            # clear_screen()
            # time.sleep(0.5)

print(calculate_points(robot_maze))

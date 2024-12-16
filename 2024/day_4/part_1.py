
letter_matrix = []
target = list('XMAS')

with open('input.txt', 'r') as f:
# with open('test', 'r') as f:

    for line in f:
        letter_matrix.append(list(line)[:len(line) - 1])

total = 0

max_y = len(letter_matrix)
max_x = len(letter_matrix[0])

directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

def look_around(target_word, letter_matrix, x, y, target_index, direction):
    
    if target_index == 4:
        return 1

    if (x < 0 or y < 0) or (x >= max_x or y >= max_y) or (target_word[target_index] != letter_matrix[y][x]):
        return 0

    return look_around(target_word,
                       letter_matrix,
                       x + direction[0],
                       y + direction[1],
                       target_index + 1,
                       direction)

for y in range(max_y):
    for x in range(max_x):
        if letter_matrix[y][x] == 'X':
            for direction in directions:
                total += look_around(target, letter_matrix, x, y, 0, direction)

print(total)
    

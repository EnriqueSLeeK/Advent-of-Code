
letter_matrix = []
target_word = list('MAS')

with open('input.txt', 'r') as f:
# with open('test', 'r') as f:
    for line in f:
        letter_matrix.append(list(line)[:len(line) - 1])

total = 0

max_y = len(letter_matrix)
max_x = len(letter_matrix[0])

directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

def check_invalid_index(x, y):
    if (x < 0 or y < 0) or (x >= max_x or y >= max_y):
        return True

def look_around(target_word, letter_matrix, x, y, target_index, direction):
    
    if target_index == 3:
        return 1

    if check_invalid_index(x, y) or (target_word[target_index] != letter_matrix[y][x]):
        return 0

    return look_around(target_word,
                       letter_matrix,
                       x + direction[0],
                       y + direction[1],
                       target_index + 1,
                       direction)

def check_diag(target_word, letter_matrix, x, y, diag_direction):

    for direction in diag_direction:
        if letter_matrix[y + direction[1]][x + direction[0]] == 'M':
            if look_around(target_word,  letter_matrix, x + direction[0], y + direction[1], 0, tuple(-x for x in direction)):
                return 1
            break
    return 0
for y in range(1, max_y - 1):
    for x in range(1, max_x - 1):
        found = 0
        if letter_matrix[y][x] == 'A':
            found += check_diag(target_word, letter_matrix, x, y, directions[:2])
            found += check_diag(target_word, letter_matrix, x, y, directions[2:])

        if found == 2:
            total += 1

print(total)
    

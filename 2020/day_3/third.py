#!/usr/bin/python3.9

def tree_encounter(layers):

    moves = [ [1, 1], [3, 1], [5, 1], [7, 1], [1, 2] ]
    tree_count = [0, 0, 0, 0, 0]
    right = 0    
    down = 1
    k = 0

    for move in moves:
        down = move[1]
        for layer in layers:

            if down == move[1]:
                
                if right >= len(layer) - 1:
                    right -= len(layer) - 1

                if layer[right] == '#':
                    tree_count[k] += 1
                
                if move[1] == 1:
                    right += move[0]               
                down = 1

            else:
                if down == 1:
                    right += move[0]
                down += 1

        k += 1
        down = 1
        right = 0

    return tree_count

input = open("third_input.txt", 'r')


t = 1
for trees in tree_encounter(input.readlines()):
     t *= trees
print("The answer is: " + str(t))

input.close()

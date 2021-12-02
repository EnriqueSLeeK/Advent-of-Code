#!/usr/bin/python3.9

# First part solution
def count(req_and_pass_list):
    valid = 0
    for req_and_pass in req_and_pass_list:
        parts = req_and_pass.split(": ")
        if check(parts[0], parts[1]):
            valid += 1
        else:
            continue
    return valid
       
def check(req, password):
    min_max_char = req.split(" ")
    min_max = min_max_char[0].split("-")
    
    counter = 0
    for character in password:
        if min_max_char[1] == character:
            counter += 1
    
    if int(min_max[0]) <= counter and int(min_max[1]) >= counter:
        return True

input = open("second_input.txt", 'r')
print( count(input.readlines()) )
input.close()
# First part end

# Second part solution
def count_2(req_and_pass_list):
    valid = 0
    
    for req_and_pass in req_and_pass_list:
        parts = req_and_pass.split(": ")
        
        if check_constraint(parts[0], parts[1]):
            valid += 1
        else:
            continue
    return valid

def check_constraint(req, password):

    min_max_char = req.split(" ")
    min_max = min_max_char[0].split("-")
    
    first_c = password[ int(min_max[0]) - 1]
    second_c = password[ int(min_max[1]) - 1]
    
    if first_c != second_c and (first_c == min_max_char[1] or second_c == min_max_char[1]):
        return True

input = open("second_input.txt", 'r')
print( count_2(input.readlines()) )
input.close()
# Second part end

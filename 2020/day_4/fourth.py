#!/usr/bin/python3.9

import re

# byr (Birth Year)              
# iyr (Issue Year)              
# eyr (Expiration Year)         
# hgt (Height)                  
# hcl (Hair Color)              
# ecl (Eye Color)               
# pid (Passport ID)             
# cid (Country ID) (optional)   


def passport_check(input_list):

    valid = 0
    data = []
    for line in input_list:
        for d in re.split(':| ', line):
            
            data.append(d)

        if line == "\n":
            print(data)
            if 'byr' in data and 'iyr' in data and 'eyr' in data and 'hgt' in data and 'hcl' in data and 'ecl' in data and 'pid' in data:
                    valid += 1
            data = []

    return valid

def passport_check(input_list):

    eye_color = ['amb', 'blu', 'gry', 'brn', 'grn', 'hzl', 'oth']
    valid = 0
    data = []
    for line in input_list:
        for d in re.split(':| |\n', line):
            
            data.append(d)

        if line == "\n":

            if 'byr' in data and 'iyr' in data and 'eyr' in data and 'hgt' in data and 'hcl' in data and 'ecl' in data and 'pid' in data:
                b_year = data[data.index('byr') + 1].replace("\n", "")
                y_issue = data[data.index('iyr') + 1].replace("\n", "")
                exp_date = data[data.index('eyr') + 1].replace("\n", "")
                height = data[data.index('hgt') + 1].replace("\n", "") 
                h_color = data[data.index('hcl') + 1].replace("\n", "") #
                e_color = data[data.index('ecl') + 1].replace("\n", "")
                passport_id = data[data.index('pid') + 1].replace("\n", "")

                
                
                if 1920 <= int(b_year) <= 2002 and \
                   2010 <= int(y_issue) <= 2020 and \
                   2020 <= int(exp_date) <= 2030 and \
                   len(passport_id) == 9 and \
                   e_color in eye_color and \
                   (('cm' in height and 150 <= int(height.replace("cm", "")) <= 193) or \
                   ('in' in height and 59 <= int(height.replace("in", "")) <= 76)) and \
                   (h_color[0] == '#' and len(h_color) == 7 and re.compile(r'[^a-f0-9.]').search(h_color)):

                       valid += 1

            data = []

    return valid
input = open('input.txt', 'r')

#input = open('t.txt', 'r')

print( passport_check(input.readlines()) )

input.close()

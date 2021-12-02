#!/usr/bin/python3.9


def multiply_1(list_expenses):

    for expense in list_expenses:
        for second_ex in list_expenses:
            if int(expense) + int(second_ex) == 2020:
                return int(expense) * int(second_ex)
    return False

def multiply_2(list_expenses):

    for expense in list_expenses:
        for second_ex in list_expenses:
            for third_ex in list_expenses:
                if int(expense) + int(second_ex) + int(third_ex) == 2020:
                    return int(expense) * int(second_ex) * int(third_ex)
    return False


input = open("first_input.txt", 'r')
print( "First part answer : " + str(multiply_1(input.readlines())) )
input.close()
input = open("first_input.txt", 'r')
print( "Second part answer: " + str(multiply_2(input.readlines())) )
input.close()

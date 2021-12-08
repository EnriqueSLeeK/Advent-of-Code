with open("input", "r") as f:
    signals_and_codes = [[sequence for sequence in code.split('|')]
                        for code in f]

signals = [signals[0].split() for signals in signals_and_codes]
codes = [signals[1].split() for signals in signals_and_codes]

def construct_num(number_one, number_four, seq_code):
    number = ""
    one_set = set(number_one)
    four_set = set(number_four)
    for code in seq_code:
        code_len = len(code)
        if (code_len == 2):
            number += "1"
        elif (code_len == 4):
            number += "4"
        elif (code_len == 3):
            number += "7"
        elif (code_len == 7):
            number += "8"
        elif (code_len == 5):
            code_set = set(code)
            if (len(code_set.difference(one_set)) == code_len - 2):
                number += "3"
            else:
                if (len(code_set.difference(four_set)) == code_len - 2):
                    number += "2"
                else:
                    number += "5"
        elif (code_len == 6):
            code_set = set(code)
            if (len(set(code).difference(set(number_one))) == code_len - 1):
                number += "6"
            else:
                if (len(code_set.difference(four_set)) == code_len - 4):
                    number += "9"
                else:
                    number += "0"
    return (number)

def find_one(seq_signal, length):
    for signal in seq_signal:
        if (len(signal) == length):
            return (signal)

total = 0
for seq_code, seq_signal in zip(codes, signals):
    interest_one = find_one(seq_signal, 2)
    interest_four = find_one(seq_signal, 4)
    total += int(construct_num(interest_one, interest_four, seq_code))
print(total)

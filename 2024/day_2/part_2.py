
def diff(a, b):
    return abs(a - b)

def check_values(a, b, mode):

    if diff(a, b) > 3:
        return True

    max_val = max(a, b)
    min_val = min(a, b)
    
    return  (max_val == min_val) or \
            (mode and min_val == a) or \
            (not mode and max_val == a)

safe = 0

def check_unsafe(report):
    a = report[0]
    mode = report[0] > report[1]
    for b in report[1:]:
        if check_values(a, b, mode):
            return True
        a = b


with open('input.txt', 'r') as f:
# with open('test', 'r') as f:

    for line in f:
        report = list(map(int, line.split()))
        for i in range(len(line)):
            new_report = report[:i] + report[i + 1:]
            if not check_unsafe(new_report):
                safe += 1
                break

    print(safe)

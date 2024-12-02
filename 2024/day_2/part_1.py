
def diff(a, b):
    return abs(a - b)

unsafe = 0

with open('input.txt', 'r') as f:
    line_count = 0
    for line in f:
        line_count += 1
        report = list(map(int, line.split()))
        a = report[0]
        mode = report[0] > report[1]
        
        for b in report[1:]:
            if diff(a, b) > 3:
                unsafe += 1
                break

            max_val = max(a, b)
            min_val = min(a, b)

            if  (max_val == min_val) or \
                (mode and min_val == a) or \
                (not mode and max_val == a):
                unsafe += 1
                break

            a = b

    print(line_count - unsafe)

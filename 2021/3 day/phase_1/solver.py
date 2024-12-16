def vertical_patter(index):
    count = [0, 0]
    with open("input", "r") as f:
        for line in f:
            count[int(line[index])] += 1
    return ("1" if count[0] > count[1] else "0")

epsilon = ""
for k in range(12):
    epsilon = epsilon + vertical_patter(k)
print(epsilon)
print(int(epsilon, 2))

gamma = ""
for k in epsilon:
    if (k == '1'):
        gamma = gamma + "0"
    else:
        gamma = gamma + "1"
print(gamma)
print(int(gamma, 2))

print(int(epsilon, 2) * int(gamma, 2))

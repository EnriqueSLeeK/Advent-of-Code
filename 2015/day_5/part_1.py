
lines = []
# lines = ['aaa']
not_allowed = set(['ab', 'cd', 'pq', 'xy'])
count = 0

with open('input', 'r') as f:
    for line in f:
        lines.append(line.rstrip())


vowels = set(['a', 'e', 'i', 'o', 'u'])

for line in lines:
    subsequent = False
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            subsequent = True

        if line[i:i + 2] in not_allowed:
            subsequent = False
            break
    
    vowel = [c for c in line if c in vowels]

    if len(vowel) > 2 and subsequent:
        count += 1

print(count)

from collections import defaultdict

with open("input", "r") as f:
    scanners = [block for block in f.read().split("\n\n")]

detected = defaultdict(lambda: [])

# Parsing to a dictionary
for scanner in scanners:
    curr = None
    for line in scanner.split("\n"):
        line = line.strip()
        if (line.startswith('--- ')):
            curr = line.lstrip("--- ").rstrip(" ---").replace(' ', '')
            detected[curr]
        else:
            if (line != ''):
                xyz = [int(num) for num in line.split(',')]
                detected[curr].append(xyz)

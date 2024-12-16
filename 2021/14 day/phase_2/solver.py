from collections import defaultdict, Counter

with open("input", "r") as f:
#with open("t", "r") as f:
    lines = [line for line in f.read().split("\n\n")]

polymer = lines[0]

reactions = defaultdict(lambda: "")

for reaction in [chem.split(" -> ") for chem in lines[1].strip().split("\n")]:
    reactions[reaction[0]] = reaction[1]

count = Counter()

def split(chain):
    parts = []
    for i in range(2, len(chain) + 1):
        parts.append(chain[i - 2: i])
    return (parts)

# Populate the dictionary
for snip in split(polymer):
    count[snip] += 1

for i in range(40):
    counter_aux = Counter()
    for pair in count:
        counter_aux[pair[0] + reactions[pair]] +=  count[pair]
        counter_aux[reactions[pair] + pair[1]] +=  count[pair]
    count = counter_aux

char_freq = Counter()
for pair in count:
    char_freq[pair[0]] += count[pair]

# Must count the final character
char_freq[polymer[-1]] += 1

print(max(char_freq.values()) - min(char_freq.values()))

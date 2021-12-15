from collections import defaultdict

with open("input", "r") as f:
#with open("t", "r") as f:
    lines = [line for line in f.read().split("\n\n")]

polymer = lines[0]

reactions = [chem.split(" -> ") 
            for chem in lines[1].split("\n")]
reactions.pop(-1)

reaction_dict = defaultdict(lambda: "")

for react in reactions:
    reaction_dict[react[0]] = react[1]

freq = defaultdict(lambda: 0)

def split(chain):
    parts = []
    for i in range(2, len(chain) + 1):
        parts.append(chain[i - 2: i])
    return (parts)

def poly_reaction(poly, flag):
    if (len(poly) == 2):
        react = reaction_dict[poly]
        tmp = list(poly)
        tmp.insert(1, react)
        if (flag == 1):
            return "".join(tmp)
        else:
            return tmp[1]
    else:
        new_polymer = ""
        for snip in split(poly):
            new_polymer += poly_reaction(snip, flag)
            flag = int(not flag)
        if (flag == 1):
            new_polymer += poly[-1]
        return (new_polymer)

for step in range(10):
    polymer = poly_reaction(polymer, 1)

for element in polymer:
    freq[element] += 1
print(max(freq.values()) - min(freq.values()))

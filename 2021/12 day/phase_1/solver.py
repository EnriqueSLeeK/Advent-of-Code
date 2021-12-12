from collections import defaultdict

with open("input", "r") as f:
    paths = [[node.replace("\n", "") for node in connection.split("-")] for connection in f]

path_branch = defaultdict(lambda: [])

for path in paths:
    if (path[0] == "start"):
        path_branch[path[0]].append(path[1])
    elif (path[1] == "start"):
        path_branch[path[1]].append(path[0])
    else:
        path_branch[path[1]].append(path[0])
        path_branch[path[0]].append(path[1])

def explore(node, visited):
    if (node == "end"):
        return (1)
    elif (node in visited):
        return (0)
    elif (node.islower()):
        visited.append(node)
    total = 0
    for section in path_branch[node]:
        total += explore(section, visited.copy())
    return (total)

total_path = 0
for start_point in path_branch['start']:
    total_path += explore(start_point, [])
print(total_path)

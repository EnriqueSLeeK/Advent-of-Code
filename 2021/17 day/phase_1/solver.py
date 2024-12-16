from collections import defaultdict

with open("input", "r") as f:
#with open("t", "r") as f:
    area = f.readline().replace("target area: ", "").strip().split(",")

x_range = [int(val) for val in area[0].strip().replace("x=", "").split('..')]
y_range = [int(val) for val in area[1].strip().replace("y=", "").split('..')]

def check(x, y):
    if (x_range[0] <= x and x_range[1] >= x and
        y_range[0] <= y and y_range[1] >= y):
        return (True)
    return (False)

def overshoot_check(velocity, limit):
    if (min(limit) >= 0):
        if (velocity > limit[1]):
            return (True)
    else:
        if (velocity < limit[0]):
            return (True)
    return (False)

# Position calculation using the inital velocity and
# the number of steps
def position_calc(initial, t):
    return (((-t * t) + t + 2 * t * initial) // 2)

# Total distance traveled until velocity is zero
def distance_until_zero(velocity):
    return ((velocity * (velocity + 1)) // 2)

# The time taken to reach to the top is the "same" value
# as the velocity
def time_to_top(velocity):
    return (velocity)

candidate_x = defaultdict(lambda: [])
for k in range(1, x_range[1] + 1):
    if (distance_until_zero(k) >= x_range[0]):
        for step in range(1, x_range[1] + 1):
            pos = position_calc(k, step)
            if (check(pos, y_range[0])):
                candidate_x[k].append(step)
            if (overshoot_check(pos, x_range)):
                break
            if (step == k):
                candidate_x[k].append(-1)
                break
    else:
        continue
#print(candidate_x, end = "\n\n")

candidate_y = defaultdict(lambda: [])
for k in range(y_range[0], abs(y_range[0])):
    for step in range(1, abs(y_range[0]) * 4):
        pos = position_calc(k, step)
        if (check(x_range[0], pos)):
            candidate_y[k].append(step)
        if (overshoot_check(pos, y_range)):
            break
#print(candidate_y)

ans = []
for key_x in candidate_x:
    if (-1 in candidate_x[key_x]):
        ans.append([key_x, list(candidate_y.keys())[-1]])

print(distance_until_zero(ans[0][1]))

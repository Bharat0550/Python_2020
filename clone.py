import copy

d = [2, 4, [7]]

t = copy.deepcopy(d)

t[-1].append(100)

print(t)

print(d)

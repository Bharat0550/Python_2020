

k = [2, 4, [3, 5]]

raw_data = str(k)

print(raw_data, type(raw_data))



lst = eval(raw_data)

lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

for i in range(len(lst)):

    tt = list(lst[i])

    tt[-1] = 100

    tt = tuple(tt)

    lst[i] = tt

print(lst)

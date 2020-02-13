
ls = [1, 2, 'hello', 'Hi', 'Python', 23, 2]



element = 2

k = 0

c = ls.count(element)

print('number of elements ', c)

for i in range(c):

    k = ls.index(element,k+1)

    print('position ', k)


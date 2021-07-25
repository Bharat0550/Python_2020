l1=[10,2,3,4,5,7]
l2=[]
for i in l1:
    for j in range(2,i):
        if i%j == 0:
            break
        else:
            l2.append(i)
 print(l2)


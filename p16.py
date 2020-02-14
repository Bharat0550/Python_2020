ls=[(10,20,40),(40,50,60),(70,80,90)]
p=[]
for i in ls:
	i=list(i)
	i[2]=10000
	i=tuple(i)
	p.append(i)
	
	
print(p)
	

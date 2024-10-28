mylist=[(), ('',),(), ('a', 'b'), ('a', 'b', 'c'), ('d')]
r=[]
for i in mylist:
    if len(i)!=0:
        r.append(i)
print(r)        
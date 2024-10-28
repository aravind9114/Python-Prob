mylist=[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
a=[]
print("list:",mylist)
for i in mylist:
    w=sum(i)
    a.append(w)
print("sum of tuples in list:",a)
mylist=[]
nlist=[]
xlist=[]
x=1
for i in range(1,31):
    x=i**2
    mylist.append(x)
    if i<=5:
        nlist.append(x)
    elif i>25:   
        xlist.append(x)
       
print(mylist)
print(nlist)
print(xlist)
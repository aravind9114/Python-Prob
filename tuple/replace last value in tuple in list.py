mylist= [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
#print([i[:-1] + (100,) for i in mylist])
klist=[]
for i in mylist:
    
        w=i[:-1]+(100,)
        klist.append(w)
print(klist)
    
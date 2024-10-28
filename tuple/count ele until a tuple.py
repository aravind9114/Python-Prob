count=0
ltup=[1,2,"a",4,("a",4),2,(3,)]
for i in ltup:
    if type(i)==tuple:
        continue
    else:
     count=count+1
print(count)

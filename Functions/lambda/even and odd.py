l=[1,2,3,4,5,6,7,8,9,10]
e=[]
o=[]
for i in l:
    x=lambda n:n%2
    print(x(i))
    if x==0:
     for i in l:
        e.append(i)
     print(e)
    else:
        for i in l:
            o.append(i)
        print(o)
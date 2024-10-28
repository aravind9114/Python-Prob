mytuple=()
ltup=list(mytuple)
rep=[]
n=int(input("enter the no of elements: "))
for i in range(n):
    ele=input("enter elements:")
    ltup.append(ele)
for i in ltup:    
    if ltup.count(i)>1:
      if i not in rep:
        rep.append(i)
        print(i)
mytuple=tuple(ltup)
print(mytuple)       
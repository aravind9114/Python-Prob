mytuple=()
ltup=list(mytuple)
rep=[]
m=1
n=int(input("enter the no of elements: "))
for i in range(n):
    ele=int(input("enter number:"))
    ltup.append(ele)
    m=m*ele
mytuple=tuple(ltup)   
print(mytuple)
print(m)    
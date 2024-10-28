mytuple=()
ltup=list(mytuple)
rep=[]
n=int(input("enter the no of elements: "))
for i in range(n):
    ele=input("enter elements:")
    ltup.append(ele)
rep=ltup[::-1]
mytuple=tuple(ltup)
print(mytuple)

print(tuple(rep))
    

mylist1=[]
n=int(input("enter the number of items:"))
for i in range(n):
    num=input("enter an element:")
    mylist1.append(num)
mytuple=tuple(mylist1)
print(mytuple)
x=mytuple[-4]
print(x)
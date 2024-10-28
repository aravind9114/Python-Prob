mylist=[]
n=int(input("eneter the number of items:"))
x=1
for i in range(n):
    num=int(input("enter a number:"))
    mylist.append(num)
    x=x*num
print(mylist)
print("product=",x)    
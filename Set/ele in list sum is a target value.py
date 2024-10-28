myset=[]
p=[]
n=int(input("enter the no of items:"))
target=int(input("enter the target value:"))
for i in range(n):
    num=int(input("enter a number:"))
    myset.append(num)
print(myset)
myset=set(myset)
for i in myset:
    x=target-i
    if x in myset:
        p.append([x,i])
print(p)
     
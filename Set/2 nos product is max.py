myset=set()
p=[]
products=1
n=int(input("enter the no of items:"))
for i in range(n):
    num=int(input("enter a number:"))
    myset.add(num)
print(myset)
for i in myset:
   for j in myset:
       if i!=j :
           products=i*j
           p.append([i ,"x",j,"=",products])
print("maximum product:",max(p))

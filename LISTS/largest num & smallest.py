mylist=[]
n=int(input("enter the number of items:"))
for i in range(n):
    num=int(input("enter a number:"))
    mylist.append(num)
print(mylist)
mylist.sort()
x=mylist[-1]
print("largest number=",x)  
mylist.sort(reverse=False) 
y=mylist[0] 
print("smallest number=",y)
mylist=[]
n=int(input("enter the number of items:"))
for i in range(n):
    num=int(input("enter a number:"))
    mylist.append(num)
print(mylist)
if len(mylist)==0:
    print("list is empty")
else:
    print("not empty")    
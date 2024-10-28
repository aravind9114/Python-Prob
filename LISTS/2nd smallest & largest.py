mylist=[]
n=int(input("enter the no of items:"))
for i in range(n):
    num=int(input("enter a number:"))
    mylist.append(num)
print("\nentered list:\t",mylist) 
mylist.sort()
print("2nd smallest number:\t",mylist[1])
mylist.sort(reverse=False)
print("\n2nd largest number:\t",mylist[-2]) 
  
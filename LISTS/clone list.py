mylist=[]
n=int(input("eneter the number of items:"))
for i in range(n):
    num=int(input("enter a number:"))
    mylist.append(num)
print(mylist)   
newlist=mylist.copy() 
print("\ncopied list=",newlist)
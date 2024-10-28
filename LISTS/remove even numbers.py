"""mylist=[]
oglist=[]
n=int(input("eneter the number of items:"))
for i in range(n):
    num=int(input("enter a number:"))
    oglist.append(num)
    mylist.append(num)
    if num%2==0:
        mylist.remove(num)
print("\nentered list:\t",oglist)        
print("\nlist after removing even numbers:\t",mylist)        """
mylist=[]
oglist=[]
n=int(input("eneter the number of items:"))
for i in range(n):
    num=int(input("enter a number:"))
    oglist.append(num)
    
    if num%2!=0:
        mylist.append(num)
print("\nentered list:\t",oglist)        
print("\nlist after removing even numbers:\t",mylist)        
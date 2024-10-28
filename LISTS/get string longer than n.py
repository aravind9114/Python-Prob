mylist=[]
oglist=[]
n=int(input("eneter the number of items:"))
l=int(input("enter a number to check:"))
for i in range(n):
    num=input("enter a string:")
    oglist.append(i)
    if len(num)>l:
     mylist.append(num)
print("entered list:",oglist)   
print("\nlength to check",l)  
print("\nstring with length greater than n",mylist)     
    
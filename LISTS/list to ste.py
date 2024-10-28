mylist=[]
n=int(input("enter the number of items:"))
for i in range(n):
    num=input("enter a character:")
    mylist.append(num)
print(mylist)    
txt="".join(mylist)
print(txt)
mylist1=[]
mylist2=[]
mylist=[]
diff=0
n=int(input("enter the number of items:"))
for i in range(n):
    num=int(input("enter a number:"))
    mylist1.append(num)
print("\nLIST 1\t",mylist1)
for i in range(n):
    num=int(input("enter a number:"))
    mylist2.append(num)
print("\nLIST 2\t",mylist2)    
for i in range(n):
    diff=mylist1[i]-mylist2[i]
    mylist.append(diff)
print("\n",mylist1,"-",mylist2,"=",mylist)    
   
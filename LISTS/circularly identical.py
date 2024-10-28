print("=====================Circularly Identical================================")
mylist1=[]
mylist2=[]
mylist=[]
n=int(input("enter the number of items:"))
for i in range(n):
    num=int(input("enter a number:"))
    mylist1.append(num)
print("\n2nd list")
for i in range(n):
    num=int(input("enter a number:"))
    mylist2.append(num)
print("\nLIST 1\t",mylist1)
print("\nLIST 2\t",mylist2) 
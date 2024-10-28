mylist=[]
n=int(input("enter the number of items:"))
count=0
for i in range(n):
    txt=input("enter a string:")
    mylist.append(txt)
    if len(txt)>=2 and txt[0]==txt[-1]:
        count=count+1
print(mylist)
print("\nnumber of string:",count)        
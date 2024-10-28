mylist=[]
oglist=[]
n=int(input("eneter the number of items:"))
for i in range(n):
    num=int(input("enter a number:"))
    oglist.append(num)
    def check_even(num):
        if num%2!=0:
            mylist.append(num)
    check_even(num)
print("\nentered list:\t",oglist)        
print("\nlist after removing even numbers:\t",mylist) 
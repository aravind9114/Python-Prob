#sort a list with out using sort method
# mylist=[]
# newlist=[]
# n=int(input("enter the no of items:"))
# for i in range(n):
#     num=int(input("enter a number:"))
#     mylist.append(num)
# print(mylist)
# for j in range(len(mylist)):
#     for k in range(1,len(mylist)):
#         if mylist[j]>mylist[k]:
#             mylist[j],mylist[k]=mylist[k],mylist[j]
#         elif mylist[j]<mylist[k]:
            

        

# print(mylist)
    
# print(newlist)/
# sorting a list basic method
# lst = [4,5,10,3,7,6,2,3,7]
# sort_l=[]
# while len(lst)>0:
#     low=lst[0]
#     for i in lst:
#         if i<low:
#             low=i
#     sort_l.append(low)
#     lst.remove(low)
# print(sort_l)

# Bubble sort
"""
lst = [4,5,10,8,2,5,0,3,7,6,2,3,7]
x=0
while x<=len(lst):
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            lst[i],lst[i+1]=lst[i+1],lst[i]
    x+=1
print(lst)"""
n=int(input())
if n %2 == 0:
    if n>5 and n<21:
        print("Weird")
    elif n>1 and n<6:
        print("not weird")
    else:
        print("not weird")
else:
    print("weird")
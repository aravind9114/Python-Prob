mylist=["car","bike","apple"]
print(mylist)
print(mylist[0:2])
print(mylist[-1])
print(mylist[:6])
print(len(mylist))
if 87 in mylist:
    print("present")
print(type(mylist))

print(mylist)
mylist[1:3]=["ball","bat"]
print(mylist)
mylist.insert(3,"bus")

print(mylist)
list1=["laptop","desktop"]
mylist.extend(list1)
print(mylist)
mylist.remove("bat")
print(mylist)
x=mylist.pop()
print(x)
for i in range(len(mylist)):
    print(i+1,mylist[i])
i=0
while i < len(mylist):
    print(mylist[i])
    i=i+1    
mylist.sort(reverse=True)    
print(mylist)
mylist.reverse()
print(mylist)
list2=["door"]
mylist=mylist+list2
print(mylist)
list3=mylist.copy()
print(list3)
print(mylist.count("bus"))
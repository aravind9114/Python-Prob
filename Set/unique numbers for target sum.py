myset=set()
myset=list(myset)
p=[]
target=int(input("enter a target value:"))
n=int(input("enter the no of items:"))
for i in range(n):
    num=int(input("enter a number:"))
    myset.append(num)

for i in range(len(myset)):
    for j in range(i+1,len(myset)):

        x=target-myset[i]-myset[j]

        if x in myset[:i] + myset[j+1:]:
            if x!=i and j!=i and x!=j:
                p.append(tuple(sorted((x,myset[i],myset[j]))))
myset=set(myset)
print("entered set:\n",myset)
p=set(p)
print("target value:\n",target)
print("output:\n",p)     
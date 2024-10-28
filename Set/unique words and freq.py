myset=[]
f={}
print(type(myset))
n=int(input("enter the no of items:"))
for i in range(n):
    num=input("enter a word:")
    myset.append(num)
for i in myset:
    f[i]=myset.count(i)
print(f)
print(myset)    
myset=set(myset)
print(myset)
myset=set()
print(type(myset))
n=int(input("enter the no of items:"))
for i in range(n):
    num=int(input("enter a number:"))
    myset.add(num)
print(myset)
print("maximum:",max(myset))
print("minimum:",min(myset))

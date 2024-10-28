myset = {"apple", "banana", "cherry",1,True,0,False}
set1={"door","kite","apple"}
set1.intersection_update(myset)
print(set1)
print(myset)
for i in myset:
    print(i)
myset.add("bike")
print(myset)
myset.update(set1)
print(myset)
myset.remove(1)
print(myset)
x=myset.pop()
print(x)
set3=myset.union(set1)
print(set3)
set1.update(myset)
print(set1)
x = {"apple", "banana", "cherry"}
y = {"door","kite","apple"}
x.symmetric_difference_update(y)
print(x)
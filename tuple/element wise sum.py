x = (1, 2, 3, 4)
y = (3, 5, 2, 1)
z = (2, 2, 3, 1)
print(x)
print(y)
print(z)
a=[]

for i in zip(x,y,z):
   w=sum(i)
   a.append(w)
print("sum:",tuple(a))

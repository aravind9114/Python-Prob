n=int(input("enter limit:"))
a=[]
for i in range(n):
   s=int(input("enter a number:"))
   a.append(s)
print("numbers are:",a)   
i = 0
while i<len(a)-1:
    if a[i] > a[i+1]:
        tmp = a[i]
        a[i] = a[i+1]
        a[i+1] = tmp
        i=0
    else:    
     i += 1
print(a)
x=len(a)//2
print("median:",a[x])

n=int(input("enter a number:"))
num=str(n)
x=len(num)
sum=0
for j in num:
  i=int(j)
  sum=sum+i**x
if sum==n:
  print("Armstrong")
else:
  print("Not an armstrong")
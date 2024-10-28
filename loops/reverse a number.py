n=int(input("enter a number:"))
s=n/100
for i in range(len(str(n))):
    x=(int(n)%10)*10
    a=x+int(n/10)%(10)
    b=a*10+int(s)
    i=i+1
print(b)
if n==b:
    print("palindrome")

else:
    print("not a palindrome")

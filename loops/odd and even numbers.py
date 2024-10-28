n=int(input("enter a range:"))
print("using for loop")
print("Even Numbers:")
for x in range(2,n,2):
    print(x,end='')
print()
print("Odd Numbers:")
for x in range(1,n,2):
    print(x,end='')    
print("using while loop")

i=1
while i<n:
    if i%2==0:
        print(i)
    elif i%2!=0:    
        print(i)
    i=i+1    
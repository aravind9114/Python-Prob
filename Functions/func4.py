def my_func(a,b,c):
    if a>b and a>c:
        print(a," is greater")
    elif b>a and b>c:
        print(b," is greater")
    else:
        print(c,"is greater")
x=int(input("enter a number:"))  
y=int(input("enter a number:")) 
z=int(input("enter a number:")) 
my_func(x,y,z)
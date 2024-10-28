#python practice
print("hello world")
x ='10'
print(x)
print(type(x))
a= str(10)
z=11
b = float(z)
print(b)
num1 =11
num2=10
print(int(num1))
num =num1+num2
print(num)
x=y=z=25
print(x)
print(y)
print(z)
x,y,z= 10,23,45
print(x)
print(y)
print(z)
print(x,y,z)
b=[12,13,14]
x=set(b)
print(type(x))
a=10
b=12
c=a+b
print(c)
c=a-b
print(c)
c=a*b
print(c)
c=a/b
print(c)
c=a//b
print(c)
c=a**b
print(c)
c=a%b
print(c)


a=10
a+=5
print(a)
a-=5
print(a)
a*=2
print(a)
a/=2
print(a)
a//=2
print(a)
a**=3
print(a)
a%=5
print(a)


z=20
print(z==19 or z==20)
print(z>19 and z<25)
print(not(z> 10 and z < 21))
x = ["bike", "car"]
y = ["bike", "car"]
z = x
print(x is z)
print(x is not y)
print(x is y)
print(x==y)
print("bike" in x)
print ("hat" in y)
a=4
b=6
print(a&b)
print(a|b)
print(a>>b)
print(a<<b)
print(a^b)
print(~a)
print(((5 + 4 - 7 + 3)*(22+56)**2)/10)


a=10
b=90
if a>b:
    print("a is smaller than b")
elif b>a:
    print("b is greater than a")
else:
    print("null")        

# ODD or EVEN and POSITIVE or NEGATIVE
x=int(input("Enter a number:"))
if x>=0:
 print("POSITIVE")
 
 if x==0:
    print("ZERO") 
 elif x%2==0:
    print("EVEN")  
 else:
    print("ODD")    
else:
 print("NEGATIVE")      

# STUDENT GRADE 
X=int(input("ENTER THE MARK:"))
if x>=90 and x<=100:
   print("A+")
elif x>=80 and x<90:
   print("A")
elif x>=70 and x<80:
   print("B+")
elif x>=60 and x<70:
   print("B")
else:
   print("SATISFACTORY")         
# greatest number
a=40
b=50
c=60
if a>b and a>c:
   print("a is greater")
elif b>a and b>c:
   print("b is greater")
else:
   print("c is greater")      

# number to alphabet
x=int(input("enter a number :"))
if x==1:
   print("ONE")
elif x==2:
   print("TWO")         
elif x==3:
   print("THREE")  
elif x==4:
   print("FOUR")  
elif x==5:
   print("FIVE")  
elif x==6:
   print("SIX")
elif x==7:
   print("SEVEN")
elif x==8:
   print("EIGHT")
elif x==9:
   print("NINE")         

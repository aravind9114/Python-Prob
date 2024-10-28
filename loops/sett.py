#Enter your code here. Read input from STDIN. Print output to STDOUT
n= list(map(int, input("len of aray").split()))
for i in range(n[0]):
    num=list(map(int, input("elements in array").split()))
    
    
for k in range(n[1]):
    A=set(map(int, input("elements in set A").split()))
    
    
for k in range(n[1]):
    B=set(map(int, input("elements in set B").split()))
    break
    
B=list(B)
A=list(A)
happy=0
sad=0
for i in num:
    for j in A:
        if i==j:
            happy=happy+1
         
for i in num:
    for j in B:
            if i==j:
                sad=sad-1
sum=happy+sad
print(sum)
                
# x = list(map(int,input().split()))
# print(x)


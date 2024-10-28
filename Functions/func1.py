def armstrong(n):
 
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
armstrong( n=int(input("enter an argument:")))
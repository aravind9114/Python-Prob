mylist=[]
f={}
n=int(input("enter the no of items:"))
for i in range(n):
     ele=input("enter element:")
     mylist.append(ele)
for i in mylist:
          
          if i in f:
               f[i]=f[i]+1
          else:
               f[i]=1
print(f)                    
               
  
mylist=[]
a={}
n=int(input("enter the number of items:"))
for i in range(n):
    num=input("enter a character:")
    mylist.append(num)
    
print(mylist)
for i in mylist:
    w=''.join(sorted(i))
    if w in a:
        a[w].append(i)
    else:
        a[w]=[i]
      
print("Anagrams Are grouped",a)        
    


              
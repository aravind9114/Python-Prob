n=int(input("enter the number of items:"))
mydict={}
for i in range(n):
    key=input("enter key:")
    value=int(input("enter an integer as value:"))
    mydict[key]=value
print(mydict)    
print("Maximum value:",max(mydict.values()))
print("Minimum value:",min(mydict.values()))
str=input("enter a string:")
txt=str.split('-')
print(txt)
s=0
for i in txt:
    s=s+1
    print(f"substring {s}:",i)
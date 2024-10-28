mylist=["car","bike","bus","car","door","bike"]
dup=[]
for i in mylist:
    if i not in dup:
        dup.append(i)
print(dup)    
txt=input("enter a string:")
print("numbers are:")
for i in txt:
    if i.isnumeric():
        print(i,end="")
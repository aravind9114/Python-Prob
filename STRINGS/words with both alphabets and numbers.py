txt=input("enter a string:")
st=txt.split(" ")

for i in st:
 if not i.isalpha() and not i.isnumeric():
  
        print(i)
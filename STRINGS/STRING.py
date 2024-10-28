name="ARAVIND@123#"
txt=""
num=""
sp=""
for i in name:
    if i.isalnum():

        if i.isalpha():
          txt=txt+i
        else:
          num=num+i
    else:
      sp=sp+i
print("numbers:",num)      
print("characters:",txt)
print("special:",sp)
"""for i in name:
    if i.isnumeric():
        print(i,end="")
print("\nalphabets are:")
for i in name:        
    if i.isalpha():
        print(i,end="")
print("\nspecial characters are:")
for i in name:
    if not i.isalnum():
        print(i,end="")"""
        



      
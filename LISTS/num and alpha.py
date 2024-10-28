txt=input("enter a string:")
num_list=[]
alpha_list=[]
special=[]
for i in txt:
    if i.isalnum():
         if i.isalpha():
          alpha_list.append(i)
         else:
          num_list.append(i)
    else:
      special.append(i)
print("number list:",num_list)
print("\nalphabets list:",alpha_list)
print("\nspecial characters list:",special)
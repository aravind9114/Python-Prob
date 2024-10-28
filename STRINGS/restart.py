txt = input("enter a string")
s=""
w=""
c=txt[0]
for x in range(0, len(txt)-1):
  if c== txt[x]:
     w=txt[1:]
     s= c+w.replace(txt[x],"$")
print(s)           
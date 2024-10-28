txt=input("enter a string:")
x=any (i.isnumeric() for i in txt)
if x:
 print("DIGITS:",x)
else:
     print("DIGITS:FALSE") 

y=any (i.isalpha() for i in txt)
if y:
 print("ALPHABETS:",y)

z=any (i.isupper() for i in txt)
if z:
 print("UPPERCASE:",z) 
else:
     print("UPPERCASE:FALSE")    
l=any (i.islower() for i in txt)
if l:
 print("LOWERCASE:",l)    
else:
 print("LOWERCASE:FALSE")         
        
if txt.isalnum():
        print("alphanumeric:TRUE")
else:
        print("alphaumeric:FALSE") 
      

a=any (ord(txt[k])>ord(txt[k+1]) for k in range(len(txt)-1) 
       if ord(txt[k])>=65 and ord(txt[k])<91 or ord(txt[k])>=97 and ord(txt[k]) < 123 )
if a:
   print("ALPHABETICAL ORDER:FALSE")  
else:
   print("ALPHABETICAL ORDER:TRUE")        
str="A string describing which \ncharacters to remove from the original string."
print(str[0:2])
print(str[:3])
print(str[2:])
print(str[::-1])
print(str.upper())
print(str.lower())
print(str.title())
print(str.capitalize())
print(str.isupper())
print(str.islower())
print(str.replace('h','p'))
print(str.split(' '))
print(str.center(20,'9'))
print(str.count('l'))
print(str.find('w'))
print("%".join(str.split(' ')))
txt = "Hello World!"
mytable = str.maketrans("W", "P")
print(txt.translate(mytable))
print(str.splitlines())
print(txt.swapcase())
print(txt.zfill(20))
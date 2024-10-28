"""file=open('test.txt','w')
file.write("File handling")
file=open('test.txt','a')
file.write("\nappending")
file=open('test.txt','r')
print(file.read())
file.close()"""
try:
    file=open('test1.txt','r')
    print(file.read())
except FileNotFoundError:
    print("Error:Create a file!!!!!!!")
finally:
    print("file handling with exception test.")
   
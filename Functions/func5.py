#Write a Python program to count repeated characters in a string.
def my_func(txt):
    
    for i in range(0, len(txt)):
   
        count = 1
  

        for x in range(i + 1, len(txt)):
            if txt[i] == txt[x]:
                count += 1
            

        if count > 1:
            print(f"Character '{txt[i]}' occurs {count} times.")
a= input("Enter a string: ")
my_func(a)
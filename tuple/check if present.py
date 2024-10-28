mytuple=(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
w=input("enter the word:")
for i in range(len(mytuple)):
    if w in mytuple[i]:
        print("present")
        break
else:
        print("not present")    
        
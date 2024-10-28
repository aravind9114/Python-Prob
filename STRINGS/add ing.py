txt=input("enter a string:")
if len(txt)<3:
    print("please enter a string of length more than 3")
else:
    if txt.endswith("ing"):
        str=txt+"ly"
        print(str)    

    else:
        str=txt+"ing"
        print(str)    
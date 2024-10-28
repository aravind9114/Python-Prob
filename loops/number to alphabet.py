# x=int(input("enter a number :"))
# if x==1:
#    print("ONE")
# elif x==2:
#    print("TWO")         
# elif x==3:
#    print("THREE")  
# elif x==4:
#    print("FOUR")  
# elif x==5:
#    print("FIVE")  
# elif x==6:
#    print("SIX")
# elif x==7:
#    print("SEVEN")
# elif x==8:
#    print("EIGHT")
# elif x==9:
#    print("NINE") 
number_words = {
    1: "ONE",
    2: "TWO",
    3: "THREE",
    4: "FOUR",
    5: "FIVE",
    6: "SIX",
    7: "SEVEN",
    8: "EIGHT",
    9: "NINE",
}

x = int(input("Enter a number: "))

if x in number_words:
    print(number_words[x])
else:
    print("Please enter a number between 1 and 9.")


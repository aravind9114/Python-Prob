year = int(input("Enter a year: "))
i=0
while i<4:
    if year%4==0 and year %100==0 or year % 400==0:
        print(f"{year} is a leap year.")
        break
    else:
        print(f"{year} is not a leap year.")   
        break



"""year = int(input("Enter a year: "))
for i in range(4):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year.")
                break
            else:
                print(f"{year} is not a leap year.")
                break
        else:
            print(f"{year} is a leap year.")
            break
    else:
        print(f"{year} is not a leap year.")
        break        """
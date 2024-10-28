n = int(input("Enter a number:"))
num_str = str(n)
rev_num = num_str[::-1]
reversed_num = int(rev_num)
print("Reversed number:", rev_num)
if n == reversed_num:
    print("Palindrome")
else:
    print("Not a palindrome")

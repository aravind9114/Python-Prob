n = int(input("Enter a number: "))

reversed_number = 0
original_number = n

while n > 0:
  digit = n % 10
  reversed_number = reversed_number * 10 + digit
  n //= 10

if reversed_number == original_number:
  print("palindrome")
else:
  print("not a palindrome")

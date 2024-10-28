n = int(input("Enter number of numbers: "))
numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print(numbers)
sum=0
for x in numbers:
    sum=sum+x
    avg=sum/n
print("average =",avg)    
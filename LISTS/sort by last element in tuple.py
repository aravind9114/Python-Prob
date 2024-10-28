n = int(input("Enter the number of tuples: "))

data = []
for i in range(n):
    m = int(input(f"Enter the number of elements in tuple {i+1}(number of elements must be equal) :"))
    tuple_elements = []
    for j in range(m):
        value = int(input(f"Enter element {j+1} of tuple {i+1}: "))
        tuple_elements.append(value)
    data.append(tuple(tuple_elements))

print("Original data:", data)

for i in range(len(data)):
    for j in range(0, len(data)-i-1):
        if data[j][1] > data[j + 1][1]:
            data[j], data[j + 1] = data[j + 1], data[j]  

print("Sorted data:", data)

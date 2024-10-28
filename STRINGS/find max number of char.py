# text = input("Enter a string: ")

# # Initialize variables
# char_counts = {}
# max_count = 0
# most_repeated_char = ''

# # Iterate through each character in the string
# for char in text:
#   # Check if the character is already in the dictionary
#   if char in char_counts:
#     char_counts[char] += 1
#   else:
#     char_counts[char] = 1

#   # Update max count and most repeated character if needed
#   if char_counts[char] > max_count:
#     max_count = char_counts[char]
#     most_repeated_char = char

# # Print the result
# print(f"Most repeated character: '{most_repeated_char}' (occurs {max_count} times)")
txt = input("Enter a string: ")
str=""
counts=[]
for i in range(0, len(txt)):
   
    count = 1
  

    for x in range(i + 1, len(txt)):
        if txt[i] == txt[x]:
            count += 1

            

    if count > 1:
        counts.append(count)
        maxcount=max(counts)
for i in range(len(counts)):
    if counts[i]==maxcount:
        print(txt[i])


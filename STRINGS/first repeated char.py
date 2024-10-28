txt = input("Enter a string: ")

for i in range(0, len(txt)):
    count = 1

    for x in range(i + 1, len(txt)):
        if txt[i] == txt[x]:
            count += 1
            break

    if count > 1:
        print(f"The first repeated character is: {txt[i]}")
        break

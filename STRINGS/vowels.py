def my_func(txt):
    count = 0
    v = ""
    vowels = "aeiouAEIOU"
    print("Vowels are:")
    for i in txt:
        if i in vowels and i not in v:
            v += i
            count += 1
            print(i, end="")
    print("\nNumber of vowels:", count)
a = input("Enter a string: ")
my_func(a)
def first_func(year):
    print("hello world",year)
first_func(2024)
def first_func(year,loc):
    print("hello world",year,loc)
first_func(2024,"Kochi")
def first_func(year,loc="Kannur"):
    print("hello world",year,loc)
first_func(2024)
def first_func(*year):
    print("hello world",year[2])
first_func(2024,2020,2023)
def first_func(year,loc):
    print("hello world",year,loc)
first_func(loc="kannur",year=2000)
def first_func(**year):
    print("hello world",year["x"])
first_func(y=2020,x=2024,z=2023)
def first_func(year,loc):
    print("hello world",year,loc)
    return year*2
print(first_func(2024,"Kochi"))

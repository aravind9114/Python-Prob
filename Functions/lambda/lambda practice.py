x = lambda a : a + 19
print(x(1))
x = lambda a,b : a + b
print(x(5,90))
def myfunc(n):
  return lambda a : a + n

y = myfunc(2)

print(y(11))
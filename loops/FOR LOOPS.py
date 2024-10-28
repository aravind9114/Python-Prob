y = ["bike", "car", "bus"]
for x in y:
  print(x)
  if x == "car":
    break

y = ["bike", "car", "bus"]
for x in y:
  if x == "car":
    continue  
  print(x)

for x in range(2, 50, 3):
  print(x)


i = ["red",  "fast"]
j = ["bike", "car"]

for x in i:
  for y in j:
    print(x, y)  
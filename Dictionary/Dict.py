mydict=dict(name="Aravind",age=25,loc="Kochi")
print(mydict)
mydict["pin"]=670009
print(mydict)
x=mydict["name"]
print(x)
x=mydict.get("age")
print(x)
v=mydict.values()
print(v)
mydict.update({"age": 26})
print(mydict)
p=mydict.popitem()
print(mydict)
print(p)
for i in mydict:
    print(i)
for i,j in mydict.items():
    print(i,j)    
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily["child3"]["name"])
myfamily["child2"]["name"]="Arush"
print(myfamily)
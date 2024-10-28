sampleData = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
mydict={}
myset=set()
for i in sampleData:
    for j in i.values():
       myset.add(j)
print(myset)
def sum_list(mylist):
    if len(mylist)==1:
        return(mylist[0])
    else:
        return mylist[0]+sum_list(mylist[1:])
l=[1,2,3,4,5,6,78,8,9]
print(sum_list(l))
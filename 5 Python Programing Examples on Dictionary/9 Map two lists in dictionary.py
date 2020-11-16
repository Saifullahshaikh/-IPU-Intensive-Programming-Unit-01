def Map_lists(lst1,lst2):
    l1= len(lst1)
    l2=len(lst2)
    if l1 != l2:
        display='Length of list must be same'
    else:
        dic={}
        for i in range(l1):
            key = lst1[i]
            value = lst2[i]
            dic[key] = value
        display= dic
    return display
course=['PF','OOP','Data structure']
marks=[90,80,95]
print(Map_lists(course,marks))

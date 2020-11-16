def create(lst):
    lst_tuple=[]
    length=len(lst)
    for i in range(length):
        sq=lst[i]**2
        tu=(lst[i],sq)
        lst_tuple.append(tu)
    return lst_tuple

lst=[2,3,4,5,6]
print(create(lst))

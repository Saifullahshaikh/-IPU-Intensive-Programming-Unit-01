def removeduplicates(lst):
    a=set(lst)
    lst= list(a)
    return lst
lst=[1,2,2,'ab','ab']
print(removeduplicates(lst))

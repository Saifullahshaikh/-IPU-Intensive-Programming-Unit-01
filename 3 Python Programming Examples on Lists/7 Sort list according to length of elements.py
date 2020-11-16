def sort_element_length(lst):
    l =len(lst)
    for i in range(l-1):
        if type(lst[i]) != int:
            if len(lst[i]) > len(lst[i+1]):
                lst[i],lst[i+1]=lst[i+1],lst[i]
    return lst


lst=[1,2,34,'abc','abcd']
print(sort_element_length(lst))

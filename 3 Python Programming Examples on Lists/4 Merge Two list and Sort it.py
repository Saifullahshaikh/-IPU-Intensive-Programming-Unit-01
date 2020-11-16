def Merge(lst1,lst2):
    lst1+=lst2
    for i in range(len(lst1)):
        for j in range(len(lst1)-1-i):
            if  lst1[j] >= lst1[j+1]:
                lst1[j],lst1[j+1]=lst1[j+1],lst1[j]
    return lst1

l1=[1,3,4,5,6,7]
l2= [2,6,0,8,9]
print(Merge(l1,l2))

def Intersection(lst1,lst2):
    intersect=[]
    for i in lst1:
        for j in lst2:
            if i== j:
                intersect.append(i)
                intersect.append(j)
    intersect=set(intersect)
    return intersect

lst1= [1,2,3,4,5,6,7,8,9]
lst2=[1,3,5,7,9]
print(Intersection(lst1,lst2))
                

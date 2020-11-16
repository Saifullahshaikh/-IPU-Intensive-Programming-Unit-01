def lenoflongest(lst):
    c=[]
    for i in lst:
        count=0
        for j in i:
            count+=1
        c.append(count)
    Max=0
    for x in c:
        if x> Max:
            Max=x
    return Max

lst=['abcd','ab','xyzabg','words']
print(lenoflongest(lst))

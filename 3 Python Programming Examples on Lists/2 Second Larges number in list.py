def SecondLargest(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j] >= lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    second_largest= lst[-2]
    return second_largest


print(SecondLargest([5,4,3,2,1]))

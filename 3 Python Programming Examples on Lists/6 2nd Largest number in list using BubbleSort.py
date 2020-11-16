def BubbleSort_2ndLargest(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j] >= lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    second_largest= lst[-2]
    return second_largest

lst= [10,1,24,6,7,8,3,5,2]
print(BubbleSort_2ndLargest(lst))

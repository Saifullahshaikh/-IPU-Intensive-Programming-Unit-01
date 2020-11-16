def EvenOdd(lst):
    even=[]
    odd=[]
    length= len(lst)
    for i in range(length):
        if lst[i]%2==0:
            even.append(lst[i])
        elif lst[i]%2 != 0:
            odd.append(lst[i])
    return even,odd
print(EvenOdd([1,2,3,4,5,6,7,8,9]))

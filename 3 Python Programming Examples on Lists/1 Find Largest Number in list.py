def LargestNumber(lst):
    Max=0
    for i in lst:
        if i>Max:
            Max=i
    return Max

lst= eval(input('Enter list of numbers: '))
print(LargestNumber(lst))

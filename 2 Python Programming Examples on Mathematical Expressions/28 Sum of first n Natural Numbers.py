def SumNaturalNumber(n):
    sum_n = n*(n+1)/2   #Formula
    return sum_n

n= eval(input('Enter number: '))
print(SumNaturalNumber(n))

# using loop
def Sum(n):
    res=0
    for i in range(1,n+1):
        if i>0:
            res+=i
    return res

print(Sum(n))

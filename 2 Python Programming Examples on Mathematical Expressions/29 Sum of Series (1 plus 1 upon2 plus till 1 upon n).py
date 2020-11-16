def Series(n):
    Sum=0
    for i in range(1,n+1):
        Sum+= 1/i
    return Sum

n= eval(input('Enter a number: '))
print(Series(n))

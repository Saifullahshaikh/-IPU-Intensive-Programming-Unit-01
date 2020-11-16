def Eulers(n):
    e = 1
    for i in range(1,n+1):
        factorial=1
        for j in range(1,i+1):
            factorial*=j
        e+=(1/factorial)
    return e

n= eval(input('Enter a number: '))
print(Eulers(n))

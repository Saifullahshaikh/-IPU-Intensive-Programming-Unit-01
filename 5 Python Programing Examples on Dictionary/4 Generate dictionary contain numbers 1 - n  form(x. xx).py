def Generate(n):
    dic={}
    for i in range(1,n+1):
        dic[i]=i*i
    return dic

n= eval(input('Enter a number: '))
print(Generate(n))

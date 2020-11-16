def Reverse(num):
    num= str(num)
    num = num[::-1]
    res = ''
    for j in range(len(num)):
        res+=num[j]
    rev = int(res)
    return rev
print(Reverse(123))  

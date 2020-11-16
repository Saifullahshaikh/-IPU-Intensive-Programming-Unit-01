def GCD(num1,num2):
    if num1 > num2:
        Range= num1
    else:
        Range=num2
    gcd=0
    for i in range(2,Range+1):
        if num1%i ==0 and num2%i ==0:
            gcd = i
    return gcd
print(GCD(8,12))

def PerfectNumber(number):
    ' Perfect numbers are those divisors sum are equal to number itself (6= 1+2+3)'
    sum_perfect=0
    for i in range(1,number):
        if number%i ==0:
            sum_perfect+=i
    if sum_perfect == number:
        ans= True
    else:
        ans= False
    return ans

print(PerfectNumber(28))
print(PerfectNumber(20))

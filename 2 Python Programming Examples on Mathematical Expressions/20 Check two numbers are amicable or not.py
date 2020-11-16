# Amicable Numbers: pair of numbers, each of which is the sum of the
# factors of the other.(e.g. 220 and 284)
def Amicable_numbers(num1,num2):
    sum1=0
    sum2=0
    for i in range(1,num1):
        if num1%i == 0:
            factor1=i
            sum1+=factor1
    for j in range(1,num2):
        if num2%j==0:
            factor2=j
            sum2+=factor2
    if sum2== num1 and sum1 == num2:
        ans= True
    else:
        ans= False
    return ans
print(Amicable_numbers(220,284))

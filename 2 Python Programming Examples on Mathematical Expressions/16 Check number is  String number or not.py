# Strong Number:
                #whose sum of all digit's factorial is equal to the num
def StrongNumber(number):
    sum_factorials=0
    for i in str(number):
        factorial=1
        i = int(i)
        for j in range(1,i+1):
            factorial*=j
        sum_factorials+=factorial
    if sum_factorials == number:
        ans = True
    else:
        ans= False
    return ans

print(StrongNumber(145))
print(StrongNumber(14))

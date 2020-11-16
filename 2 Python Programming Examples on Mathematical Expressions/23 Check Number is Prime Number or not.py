def PrimeNumber(num):
    for i in range(2,num+1):
        if num%i !=0:
            ans= str(num)+' is prime number'
        else:
            ans = 'No '+ str(num)+ ' is not a prime number'
        return ans
n= eval(input('Enter a Number: '))
print(PrimeNumber(n))


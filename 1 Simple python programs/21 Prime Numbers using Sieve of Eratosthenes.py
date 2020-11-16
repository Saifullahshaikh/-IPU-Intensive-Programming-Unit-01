num=eval(input('Enter number: '))
prime=[1 for i in range(num+1)]
p=2
while p*p <= num:
    if prime[p] == 1:
        for i in range(p*p,num+1,p):
            prime[i]= False
    p+=1
for j in range(2,num+1):
        if prime[j]:
            print(j,end=' ')
            

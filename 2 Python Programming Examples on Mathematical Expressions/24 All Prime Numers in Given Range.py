def AllPrime(start, end):
    for i in range(start, end+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=' ')
            
s= eval(input('Enter starting range number: '))
e= eval(input('Enter ending range number: '))
AllPrime(s,e)

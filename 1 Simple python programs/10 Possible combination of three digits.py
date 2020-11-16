def Combinations(digits):
    if len(str(digits)) == 3:
        for i in range(1,len(str(digits))+1):
            for j in range(1,len(str(digits))+1):
                for k in range(1,len(str(digits))+1):
                    print(i,j,k)
    else:
        print('number is ot three digit')

Combinations(123)
    

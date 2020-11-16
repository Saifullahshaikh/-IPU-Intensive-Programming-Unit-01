num = eval(input('Enter number: '))
Sum=0
for i in range(1,num+1):
    Sum+=i
    for j in range(1,i+1):
        print(j,end=' ')
        if j<i:
            print('+',end=' ')
    print('=',Sum)
  

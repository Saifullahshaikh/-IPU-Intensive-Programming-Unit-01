def Divisible7_Multiple5(start, end):
    for i in range(start,end+1):
        if i%5==0 and i%7 ==0:
            print(i,end=' ')

start= eval(input('Enter starting range: '))
end= eval(input('Enter ending range: '))
Divisible7_Multiple5(start,end)

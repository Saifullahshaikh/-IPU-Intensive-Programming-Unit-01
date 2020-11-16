def odd_numbers(Range):
    for i in range(1,Range+1):
        if i%2 != 0:
            print(i,end=' ')
        else:
            print('')
odd_numbers(30)

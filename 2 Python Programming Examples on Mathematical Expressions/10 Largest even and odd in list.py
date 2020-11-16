def Largest_even_odd(lst):
    even= 0
    odd=0
    for i in lst:
        if i%2==0  and i>even:
            even= i
        if i%2!=0 and i>odd:
            odd = i
    return 'Largest Even: {}\nLargest Odd: {}'.format(even, odd)

lst=eval(input('Enter list of numbers: '))
print(Largest_even_odd(lst))
        

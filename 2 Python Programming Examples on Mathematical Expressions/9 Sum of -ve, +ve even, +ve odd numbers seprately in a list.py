def Sum(lst):
    sum_negative=0
    sum_even_positive=0
    sum_odd_positive=0
    for i in lst:
        if i <0:
            sum_negative+=i
        elif i>0 and i%2 == 0:
            sum_even_positive+=i
        elif i>0 and i%2 != 0:
            sum_odd_positive+=i
    print('Sum of Negative = {}\nSum of Positive Even = {}'
          '\nSum of Positive Odd = {}'.format(sum_negative,sum_even_positive,
                                              sum_odd_positive))
lst= eval(input('Enter list of numbers: '))
Sum(lst)

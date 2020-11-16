def Calculate_lower_upper(string):
    count_l= 0
    count_u=0
    lower= 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in string:
        if i in lower:
            count_l+=1
        elif i in upper:
            count_u+=1
    return 'Lowercase Letters: {}\nUppercase Letters: {}'.format(count_l,
                                                                 count_u)

s= 'Python Programming'
print(Calculate_lower_upper(s))
        

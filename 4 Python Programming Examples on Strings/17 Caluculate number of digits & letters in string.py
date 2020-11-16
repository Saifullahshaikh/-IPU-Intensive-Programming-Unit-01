def Calculate_digits_letters(string):
    count_d=0
    count_l=0
    digits='0123456789'
    letters= 'abcdefghijklmnopqrstuvwxyz'
    for i in string:
        if i in digits:
            count_d+=1
        elif i.lower() in letters:
            count_l+=1
    return 'Digits: {}\nLetters: {}'.format(count_d,count_l)

s= '123 Hello 432 abc 9802'
print(Calculate_digits_letters(s))

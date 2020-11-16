def letters_in_first():
    str1= input('Enter first string: ')
    str2= input('Enter second string: ')
    set1=set(str1)
    set2=set(str2)
    c_l=set1-set2
    return c_l
print(letters_in_first())

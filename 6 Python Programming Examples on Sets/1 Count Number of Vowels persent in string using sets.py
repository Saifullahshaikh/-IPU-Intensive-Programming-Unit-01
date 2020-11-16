def Count_Vowels(string):
    count=0
    vowels={'a','e','i','o','u','A','E','I','O','U'}
    l =len(string)
    for i in range(l):
        if string[i] in vowels:
            count+=1
    return 'Vowels: {}'.format(count)

s= 'hi my name is SAIFULLAH SHAIKH'
print(Count_Vowels(s))

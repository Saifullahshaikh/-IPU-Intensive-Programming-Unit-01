def count_vowels(string):
    vowels= 'aeiou'
    count=0
    for i in string:
        if i != ' ':
            char=i.lower()
            if char in vowels:
                count+=1
    return 'Number of vowels: {}'.format(count)

s= 'HellO World'
print(count_vowels(s))

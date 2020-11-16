def replace_blank_hyphen(string):
    new=''
    for i in string:
        if i == ' ':
            new+= '-'
        else:
            new+=i
    return new

s= 'Python Programming'
print(replace_blank_hyphen(s))

def Count_Lowercase(string):
    count=0
    lowercase ='abcdefghijklmnopqrstuvwxyz'
    for i in string:
        if i in lowercase:
            count+=1
    return 'Lowercase Character: {}'.format(count)

s= 'Hello World'
print(Count_Lowercase(s))

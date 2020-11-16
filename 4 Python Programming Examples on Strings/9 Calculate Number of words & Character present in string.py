def Count_Words_Char(string):
    char=0
    word=0
    for i in string:
        char+=1
        if i ==' ' or i==string[-1]:
            word+=1
    return 'Words: {}\nCharacters: {}'.format(word,char)

s= 'Hello, My name is saif'
print(Count_Words_Char(s))

dic={}
def first_char_key(word):
    k=2
    key=word[0]
    if key not in dic.keys():
        dic[key]= [word]
    else:
        lst=dic[key]
        lst.append(word)
    return dic

word= 'saif'
print(first_char_key(word))
print(first_char_key('safe'))
    

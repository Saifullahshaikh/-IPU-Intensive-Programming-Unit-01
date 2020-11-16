def Occurrences_word(string):
    word=''
    words=[]
    occ=[]
    l= len(string)
    for i in range(l):
        if string[i]!= ' ':
            word+=string[i]
        if string[i] == ' ' or i==l-1:
            words.append(word)
            word=''
    count=0
    for j in words:
        count= words.count(j)
        occ.append((j,count))
    return set(occ)

s= 'hello world hello'
print(Occurrences_word(s))

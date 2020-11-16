def ithOccurrence(i, word,lst):
    count=0
    for x in range(len(lst)):
        if lst[x]==word:
            count+=1
            if count==i:
                lst[x] =''
    return lst
            
lst= ['word','saif','word']
i=2
word='word'
print(ithOccurrence(i,word,lst))

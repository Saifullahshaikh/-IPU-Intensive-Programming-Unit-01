def form_new(string):
    new=''
    l=len(string)
    for i in range(l):
        if i <2:
            new+=string[i]
        elif (string[-2]== string[i]) or (string[-1]== string[i]):
                new+=string[i]
    return new

s= 'Python'
print(form_new(s))

def Exchange(string):
    new=''
    l = len(string)
    first= string[0]
    last=string[-1]
    new+=last
    for i in range(1,l-1):
        new+=string[i]
    new+=first
    return new
s= 'hello how are you?'
print(Exchange(s))

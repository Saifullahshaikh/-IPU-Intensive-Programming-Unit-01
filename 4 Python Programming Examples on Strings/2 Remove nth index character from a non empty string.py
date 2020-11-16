def remove_index(index, string):
    l = len(string)
    new = ''
    if index < l:
        for i in range(l):
            if i != index:
                new+=string[i]
    return new

s= 'hello how are you?'
print(remove_index(5,s))

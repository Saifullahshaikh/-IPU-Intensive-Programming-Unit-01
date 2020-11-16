def Remove_Odd(string):
    l = len(string)
    new=''
    for i in range(l-1):
        if i%2==0:
            new+=string[i]
    string=new
    return string

s= 'Helloworld'
print(Remove_Odd(s))

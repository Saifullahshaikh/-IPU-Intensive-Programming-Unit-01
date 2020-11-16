string= input('Enter a String: ')
new= ''
for i in range(len(string)):
    if string[i] == 'a':
        new+='$'
    else:
        new+=string[i]
print(new)

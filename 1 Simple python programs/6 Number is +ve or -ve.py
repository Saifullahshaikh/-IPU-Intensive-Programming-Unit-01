def Check(num):
    if num > 0:
        res = 'Positve'
    elif num < 0:
        res= 'Negative'
    elif num == 0:
        res = 'The number is Zero'
    return res
x = Check(5)
print(x)
y= Check(-8)
print(y)
z= Check(0)
print(z)

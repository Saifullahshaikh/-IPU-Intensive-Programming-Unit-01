# Exchange numbers without Temperary Variable
def Exchange(a,b):
    a,b = b,a
    return a,b
x= Exchange(1,2)
print("Exchange Numbers without Temperary Variables: ",x)

# Exchange numbers with Temperary Variable
def Exchange_with(a,b):
    c = a
    a = b
    b = c
    return a,b
y = Exchange_with(1,2)
print("Exchange Numbers with Temperary Variables: ",y)

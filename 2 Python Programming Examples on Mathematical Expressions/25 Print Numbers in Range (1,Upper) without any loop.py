def Printnumbers(upper):
    if upper >0:
        print(upper,end=' ')
        Printnumbers(upper-1)

Printnumbers(20)

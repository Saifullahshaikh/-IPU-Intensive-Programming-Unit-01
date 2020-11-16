def Pascals_triangle(row):
    for i in range(1,row+1):
        k=1
        for j in range(1,i+1):
            print(' '*(row-i),k,' '*(j),end='')
            k=(k*(i-j)//j)
        print('')

Pascals_triangle(5)

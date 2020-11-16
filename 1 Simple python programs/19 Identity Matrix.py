col =eval(input('Enter number of columns: '))
row= eval(input('Enter number of rows: '))
matrix= [[0 for i in range(col)]for j in range(row)]
for x in range(len(matrix)):
    for y in range(x+1):
        if x==y:
            matrix[x][y]=1
for a in range(row):
    for b in range(col):
       print(matrix[a][b],end=' ')
    print()

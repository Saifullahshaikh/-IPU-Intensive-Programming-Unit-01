def inverted_Star(n):
    m = 0
    for i in range(n,-1,-1):
        for j in range(m,0,-1):
            print(end=' ')
        m+=1
        for k in range(1,i+1):
            print('*',end= ' ')
        print()
print('3. Inverted Star Pattern\n')
inverted_Star(6)

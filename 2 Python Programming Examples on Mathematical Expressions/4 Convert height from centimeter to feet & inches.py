def Convert_Height(height):
    feet= height//30.48
    rem =height%30.48
    inches = rem/2.54
    while  inches >=12:
        inches=inches//12
        feet+=1
    return 'Height is {}ft & {}inches'.format(int(feet),round(inches,2))
print(Convert_Height(130))

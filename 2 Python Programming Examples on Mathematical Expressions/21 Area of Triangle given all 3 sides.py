def Area_triangle(a,b,c):
    semiperimeter = s= (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    return round(area,3)

print(Area_triangle(2,3,4))

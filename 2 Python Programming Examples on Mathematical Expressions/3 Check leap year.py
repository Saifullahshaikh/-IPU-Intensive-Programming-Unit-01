def Leap_year(year):
    if year%4 == 0:
        res= True
    else:
        res = False
    return res

print(Leap_year(2010))
print(Leap_year(2016))
print(Leap_year(2020))

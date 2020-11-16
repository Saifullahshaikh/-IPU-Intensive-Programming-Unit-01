def Convert_temperature(celcius):
    farenheight = (celcius*(9/5))+32
    return str(farenheight)+'F'

print(Convert_temperature(100))
print(Convert_temperature(45))

def GravitationalForce(mass1, mass2, distance):
    m1=mass1
    m2= mass2
    d= distance
    constant = G = 6.37*10**-11
    force = (G*m1*m2)/(d**2)
    return force
m1= eval(input('Enter the mass of 1st object in kg: '))
m2 = eval(input('Enter the mass of 2nd Object in kg: '))
d= eval(input('Enter the distance between object in meter: '))
print(GravitationalForce(m1,m2,d))

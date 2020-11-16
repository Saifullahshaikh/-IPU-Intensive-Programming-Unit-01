def Compute_Polynomial(lst):
    degree=len(lst)
    eq=0
    for i in range(degree):
        eq+= lst[i]**(degree-i)
    return eq
print(Compute_Polynomial([-1,0,2,3.4]))

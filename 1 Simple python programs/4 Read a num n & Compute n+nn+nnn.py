def Compute(num):
    n=int(num)
    solve = 0
    for i in range(1,10+1):
        cal  = n**i
        solve += cal
        print(solve)

Compute(5)


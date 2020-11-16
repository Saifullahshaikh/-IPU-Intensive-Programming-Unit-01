def Numbers(Range,divisible):
    for i in range(1,Range+1):
        if i%divisible==0:
            print(i)

Numbers(10,2)

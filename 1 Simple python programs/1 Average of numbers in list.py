def Calculate_average(lst):
        count =0
        Sum = 0
        for i in lst:
                count += 1
                Sum += i
        average = Sum/count
        return average


x = [12,34,56,78,90,10,20]
y = Calculate_average(x)
print(round(y,3))

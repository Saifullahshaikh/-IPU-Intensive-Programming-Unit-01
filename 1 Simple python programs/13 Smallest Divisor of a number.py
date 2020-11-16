def smallest_divisor(num):
    for i in range(2,100):
        if num%i == 0:
            return str(i)+" is the smallest divisor"

print(smallest_divisor(69))

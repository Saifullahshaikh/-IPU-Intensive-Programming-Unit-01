def sum_digits(num):
    Sum=0
    for i in str(num):
        Sum+=int(i)
    return Sum
print(sum_digits(123))

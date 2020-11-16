def Count(num, lst):
    count=0
    for i in lst:
        if i == num:
            count+=1
    return count


lst= eval(input('Enter the list of numbers: '))
n=eval(input('Enter number to count occurence: '))
print(Count(n,lst))

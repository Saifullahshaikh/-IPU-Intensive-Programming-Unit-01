def Armstrong_number(number):
    armstrong=0
    num=number
    length= len(str(number))
    while num >0:
        digit= num%10
        armstrong+=(digit**length)
        num=num//10
    if armstrong == number:
        res= True
    else:
        res=False
    return res

print(Armstrong_number(35))

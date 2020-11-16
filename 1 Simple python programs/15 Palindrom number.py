def Palindrome_number(num):
    check =num
    pal=0
    while num>0:
        rem=num%10
        pal=pal*10+rem
        num=num//10
    if check == pal:
        res= True
    else:
        res=False
    return res

print(Palindrome_number(122))
print(Palindrome_number(212))

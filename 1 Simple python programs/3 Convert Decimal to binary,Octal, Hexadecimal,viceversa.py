def decimal_binary(num):
    binary=''
    while num != 1:
        rem= num%2
        num=num//2
        binary+=str(rem)
    binary=binary+str(num)
    return binary[::-1]
db=decimal_binary(202)
print('Decimal to Binary: ',db)

def binary_decimal(binary):
    decimal=0
    b=str(binary)
    binary=b[::-1]
    for i in range(0,len(binary)):
        digit=int(binary[i])
        decimal+= (digit*(2**i))
    return(decimal)
bd=binary_decimal(11001010)
print('Binary to Decimal: ',bd)

def decimal_octal(decimal):
    octal = ''
    while decimal != 0:
        rem = decimal%8
        decimal= decimal//8
        octal+=str(rem)
    return octal[::-1]
do=decimal_octal(101)
print('Decimal to Octal: ',do)

def octal_decimal(octal):
    octal=str(octal)
    octal=octal[::-1]
    decimal= 0
    for i in range(0,len(octal)):
        decimal +=int(octal[i])*(8**i)
    return decimal
od=octal_decimal(145)
print('Octal to Decimal: ',od)

def decimal_hexadecimal(decimal):
    hexa=''
    form=['A','B','C','D','E','F']
    while decimal !=0:
        rem= decimal%16
        if rem > 9:
            rem = form[rem-9-1]
        decimal=decimal//16
        hexa+=str(rem)
    return hexa[::-1]
dh=decimal_hexadecimal(590)
print('Decimal to Hexa-Decimal: ',dh)

def hexadecimal_decimal(hexa):
    hexa=str(hexa)
    reverse= hexa[::-1]
    form=['A','B','C','D','E','F']
    decimal= 0
    for i in range(0,len(reverse)):
        if reverse[i] in  form:
            rem = form.index(reverse[i])
            rem+=9+1
        else:
            rem=int(reverse[i])
        decimal += rem*(16**i)
    return decimal
hd=hexadecimal_decimal('BC')
print('Hexa-Decimal to Decimal: ',hd)


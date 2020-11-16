def LCM(num1,num2):
    multiple= max(num1,num2)
    lcm= 0
    while multiple != lcm:
        if multiple % num1 == 0 and multiple % num2 == 0:
            lcm = multiple
            break
        multiple+=1
    return lcm
print(LCM(6,10))


''''while (num1 or num2) > 0:
        if num1%multiple==0 and num2%multiple== 0:
            lcm*=multiple
        elif num1%multiple!= 0 and num2%multiple==0:
            lcm*=multiple
            multiple+=1
        elif num2%multiple!= 0 and num1%multiple==0:
            lcm*=multiple
            multiple+=1
        elif num2%multiple!= 0 and num1%multiple!=0:
            multiple+=1
        num1=num1//multiple
        num2= num2//multiple
    return lcm'''

def lcm(n1,n2):
    greater=max(n1,n2)
    while True:
        if greater % n1==0 and greater%n2 == 0:
            lcm=greater
            break
        greater+=1
    return lcm
#print(lcm(6,10))

import math
def Numbers(lower,upper):
    for i in range(lower,upper+1):
        p_sq=math.sqrt(i)
        if type(p_sq)== int:
            num=i
            sum_digit=0
            while num>0:
                rem=num%10
                sum_digit+=rem
                num=num//10
            if (sum_digit<10):
                print(i)
low=1
up=1000
Numbers(low,up)
            

def display_larger(str1, str2):
    count1=0
    count2=0
    for i in str1:
        count1+=1
    for j in str2:
        count2+=1
    if count1> count2:
        display = str1
    elif count1==count2:
        display= 'Both strings are of same length'
    else:
        display = str2
    return display

s1= 'Hello'
s2= 'hello World'
print(display_larger(s1,s2))

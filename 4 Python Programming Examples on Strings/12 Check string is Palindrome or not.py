def Check_palindrome(string):
    new=''
    l=len(string)-1
    for i in range(l,-1,-1):
        new+=string[i]
    if new==string:
        ans= 'Yes, String is palindrome '+string
    else:
        ans= 'No, String is not Palindrome '+string +' '+new
    return ans

s= 'civic'
s2= 'bat'
print(Check_palindrome(s))
print(Check_palindrome(s2))

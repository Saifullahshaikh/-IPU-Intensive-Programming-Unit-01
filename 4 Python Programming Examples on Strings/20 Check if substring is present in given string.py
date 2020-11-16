def check(string,substr):
    if substr in string:
        ans=True
    else:
        ans = False
    return ans
s='Hello'
sub='ll'
print(check(s,sub))

def check_key(key, dic):
    if key in dic:
        res = True
    else:
        res = False
    return res
k='age'
d= {'name':'saif','age':20,'city':'karachi','university':'UIT'}
print(check_key(k,d))

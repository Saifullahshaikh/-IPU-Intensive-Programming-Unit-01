def remove(key,dic):
    if key in dic.keys():
        del dic[key]
    return dic
k='name'
d={'name':'saif'}
print(remove(k,d))

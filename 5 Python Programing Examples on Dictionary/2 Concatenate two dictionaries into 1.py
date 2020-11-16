def Concatenate(dict1, dict2):
    k=2
    for key,value in dict2.items():
        if key not in dict1.keys():
             dict1[key]=value
        else:
            s= str(key)
            s+=str(k)
            k+=1
            dict1[s]=value
    return dict1
d1= {'name':'saif','age':21}
d2={'name':'baber','city':'karachi'}
print(Concatenate(d1,d2))

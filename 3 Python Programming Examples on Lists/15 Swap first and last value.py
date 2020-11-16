def Swap(lst):
   a= lst[0]
   lst[0] =lst[-1]
   lst[-1]=a
   return lst

lst=[1,2,3,4,5]
print(Swap(lst))

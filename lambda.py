a=lambda x:x+5
print(a(2))

b=lambda a,b:a+b
print(b(2,3))

c=lambda a,b:a if(a>b) else b
print(c(3,1))

d=lambda a:a*a
print(d(5))

lst=[1,2,3,4,5,6]
l=list(map(lambda x:x+5,lst))
print(l)

lst=[1,2,3,4,5,6]
l=list(filter(lambda x:x%2,lst))
print(l) 

lst=(1,2,3,4,5,6)
from functools import reduce
y=reduce(lambda x,y:x+y,lst)
print(y)
     

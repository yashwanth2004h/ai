
a=[1,1,1,1]
b=[1,2,3,4]
c=[1,1,1,1]
l=list(map(lambda x,y,z:x+y+z,a,b,c))
print(l)

fruits=["mango","apple","orange","kiwi"]
e=list(filter(lambda x:'g' in x,fruits))
print(e)

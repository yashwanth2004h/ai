import numpy as np
arr=np.array ([[ 1,2,3],[4,2,5]])
print ("array is if type:",type(arr))
print ("no.of dimensions:",arr.ndim)
print ("shape of array:",arr.size) 
print ("size of the array",arr.size)
print(arr.T)
print(arr.sum())
print(arr.sum(axis=1))
print(arr.max())
print(arr.min())
print(arr.max(axis=1))
print(arr.min(axis=1))
print(arr.cumsum())
           

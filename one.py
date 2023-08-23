import pandas as pd
import numpy as np

dict={'first score':[np.nan,np.nan,np.nan,50],
      'second score':[np.nan,50,90,np.nan],
      'third score':[np.nan,20,56,30],
      'fourth score':[np.nan,np.nan,np.nan,np.nan]}           

data=pd.DataFrame(dict)
print(data)
print(data.isnull())
print(data.notnull())

print(data.fillna(0))
print(data.fillna(method='pad'))
print(data.fillna(method='bfill'))

print(data.replace(to_replace=np.nan,value=99))
print(data)
print(data.dropna(how='all'))


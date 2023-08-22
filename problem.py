import pandas as pd
data={'days':[1,2,3,4,5,6,7,8,9,10],
        'steps':[4335,9552,7332,4504,5335,7552,8332,6504,8965,7689]}
p=pd.DataFrame(data)
p['steps']=p['steps']+1000
print(p)

y=p[p['steps'] >7000]['days']
print("days walk more than 7000 steps ")

z=pd.Series(y)
print(z)

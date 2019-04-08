import pandas as pd
p=pd.Series([10,20,30,40,50,60])
print(p)
print(p.index)
print(p[0])
print(sum(p))
print(max(p))
print(min(p))
print(p.describe())
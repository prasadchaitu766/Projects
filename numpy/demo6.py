import pandas as pd
df1 = pd.DataFrame(
{
'Key1':['K0','K0','K1','K2'],
'Key2':['K0','K1','K0','K1'],
'A':['A0','A1','A2','A3'],
'B':['B0','B1','B2','B3']})

df2 = pd.DataFrame(
{
'Key1':['K0','K1','K1','K2'],
'Key2':['K0','K0','K0','K0'],
'C':['C0','C1','C2','C3'],
'D':['D0','D1','D2','D3']})



print(pd.merge(df1,df2,how='outer',on=['Key1','Key2']))
print(pd.merge(df1,df2,how='left', on=['Key1','Key2']))
print(pd.merge(df1,df2,how='right',on=['Key1','Key2']))
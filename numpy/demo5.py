import pandas as pd
# left=pd.DataFrame(
#     {
#         "students":["prasad","mani","sekhar"],
#         "courses":["python","django","project"]
#     }
# )
# right=pd.DataFrame(
#     {
#         "timing":["7 AM","11AM","3PM"],
#         "status":["Completed","Going On","Will Join"]
#     }
# )
# print("---left-------")
# result=left.join(right)
# print(result)
# print("---------------------------------------")
# print("--right---")
# result2=right.join(left)
# print(result2)
df1 = pd.DataFrame(
{ 'A':['A0','A1','A2','A3','A4'],
  'B':['B0','B1','B2','B3','B4'],
  'C':['C0','C1','C2','C3','C4'],
  'D':['D0','D1','D2','D3','D4']
},
index=[0,1,2,3,4])

df2 = pd.DataFrame(
{ 'A':['A5','A6','A7','A8','A9'],
  'B':['B5','B6','B7','B8','B9'],
  'C':['C6','C6','C7','C8','C9'],
  'D':['D6','D7','D8','D8','D9']
},
index = [3,4,5,6,7])


df3 = pd.DataFrame(
{ 'A':['A10','A11','A12','A13','A14'],
  'B':['B10','B11','B12','B13','B14'],
  'C':['C10','C11','C12','C13','C14'],
  'D':['D10','D11','D12','D13','D14']
},
index = [5,6,7,8,9])

#
# print(pd.concat([df1,df2,df3]))

print('---outer----')
outerjoin= pd.concat([df1,df2], axis=0, join='outer')
print(outerjoin)

outerjoin = pd.concat([df1,df2],join='outer', axis=1)
print(outerjoin)

print('----inner----')
innerjoin = pd.concat([df1,df2],axis = 1, join='inner')
print(innerjoin)
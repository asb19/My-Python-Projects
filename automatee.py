import pandas as pd

# source
df = pd.read_excel('source.xlsx',sheet_name='source')
#dest
df1 = pd.read_excel('d1.xlsx',sheet_name='d1')
print(df1.columns)
# print(df.head())
# r=df.loc[df['active_teachers']=='cl025uk6p1237157b60r6ur6aagi']
# print(r.iloc)
for i in range(len(df)) :
  phone=df.loc[i, "phone"]
  amount=df.loc[i, "amount"]
  
  idx=df1.index[df1["phone "]==phone]
  df1.loc[idx,['Amount']]=[amount]
df1.to_excel("output.xlsx",engine='xlsxwriter')

print(df1.head())


# here
# idx=df.index[df['active_teachers']=='ckee40n3907234n7fhcwfbzbu']
# df.loc[idx,['teachers_name']]=['Python']

# print(df)

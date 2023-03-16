
from numpy import NaN
import pandas as pd
import numpy as np

# source
df = pd.read_excel('t2.xlsx',sheet_name='source')
#dest
df1 = pd.read_excel('t1.xlsx',sheet_name='d1')
print(df1.columns)
empty=[]
# print(df.head())
# r=df.loc[df['active_teachers']=='cl025uk6p1237157b60r6ur6aagi']
# print(r.iloc)
for i in range(len(df1)):
    try:
        phone=df1.loc[i, "phone"]
        # amount=df1.loc[i, "Amount"]
        if type(phone)==str:
            phone=float(phone)
        
        df['phone'] = pd.to_numeric(df['phone'], errors='coerce')
        idx=df.index[df["phone"]==phone]
        if len(idx)==0:
            empty.append({"PHONE": phone, "AMOUNT": NaN})
    except:
        continue
# df1.to_excel("output.xlsx",engine='xlsxwriter')
df2 = pd.DataFrame(empty)
df2.to_excel('empty.xlsx', engine='xlsxwriter')

print(df1.head())


import pandas as pd


df = pd.read_excel('P1.xlsx',sheet_name='P1')
arr=[]

for i in range(10):

    arr.append(df.loc[i, "active_teachers"])

print(arr)
print(len(arr))
import pandas as pd


df1 = pd.read_excel("FOR PK.XLSX");
TID = list(df1['Talent ID'])
print(603021526 in TID)

df = pd.read_excel("surabhi pk.xlsx")
lsum=0
rsum=0
for i in range(len(df)):
    if df.iloc[i,2] in TID:
        lsum+=df.iloc[i,4]
    elif df.iloc[i, 3] in TID:
        rsum+=df.iloc[i,5]

print(lsum+rsum)


# df = pd.concat(pd.read_excel("Feb- PK matches.xlsx",sheet_name=None), ignore_index=True)
#
# # print(df['Left Talent ID'])
#
# fdf1 = df[df["Left Talent ID"].isin(TID)]
# fdf2 = df[df["Right Talent ID"].isin(TID)]
# #
# result = pd.concat([fdf1, fdf2], ignore_index=True)
# #
# result.to_excel("surabhi pk.xlsx");
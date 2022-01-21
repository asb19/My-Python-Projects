import pandas as pd


df = pd.read_excel("Surabhi.xlsx",sheet_name= 'Agency Share')
df.dropna(subset = ["Agency ID"], inplace=True)
# print(df)
df1 = df[["Agency ID","Name"]]
# d = df.to_dict('records')
d = dict(zip(*df1.values.T))
# print(d)
# print(dict(zip(*df.values.T)))
df2 = pd.read_excel("Surabhi.xlsx",sheet_name='Talent Salary')
# print(df2)
df2.dropna(subset = ["Talent ID"], inplace=True)
# print(df2)
# print(len(df["Agency ID"].unique()))
# print(df2)
print(len(df2["Agency ID"].unique()))

# fdf = df[df["Agency ID"]==14170]
for i in df2["Agency ID"].unique():
    # money_fmt = workbook.add_format({'num_format': '$#,##0', 'bold': True})
    fdf = df2[df2["Agency ID"] == i]
    print(i)

    writer = pd.ExcelWriter("%s-%s.xlsx"%(i,d[i]), engine ='xlsxwriter')
    fdf.to_excel(writer,sheet_name='Talent Salary')
    workbook = writer.book
    worksheet = writer.sheets['Talent Salary']
    money_fmt = workbook.add_format({'num_format': '#0', 'bold': True})
    worksheet.set_column('B:B', 12, money_fmt)
    f1 = df[df["Agency ID"] == i]
    f1.to_excel(writer, sheet_name='Agency Share')
    writer.save()
    # print(fdf)


# fdf.to_excel("output.xlsx")
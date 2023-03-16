import pandas as pd



df = pd.read_excel('d1.xlsx', sheet_name='d1')

for i in range(10):
    # df['phone'] = df['phone'].astype(int)
    # pd.to_numeric(df["phone"])
    # phone = df.loc[i,"phone"]
    # if type(phone)==str:
    #     phone=int(phone)
    df['phone'] = pd.to_numeric(df['phone'], errors='coerce')
    phone = df.loc[i,"phone"]
    print(phone)
    print(type(phone))
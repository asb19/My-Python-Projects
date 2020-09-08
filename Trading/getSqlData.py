import sqlite3
import pandas as pd
import numpy as np
from pprint import pprint


def ST(df, f, n):  # df is the dataframe, n is the period, f is the factor; f=3, n=7 are commonly used.
    # Calculation of ATR

    df['H-L'] = round((df['high'] - df['low']),2)
    df['H-PC'] = round(abs(df['high'] - df['close']), 2)
    df['L-PC'] = round(abs(df['low'] - df['close']), 2)

    for i in range(1,len(df)):
        df['H-PC'][i] = round(abs(df['high'][i] - df['close'][i-1]), 2)

    for i in range(1,len(df)):
        df['L-PC'][i] = round(abs(df['low'][i] - df['close'][i-1]), 2)

    df['TR'] = df[['H-L', 'H-PC', 'L-PC']].max(axis=1)
    df['ATR'] = np.nan
      # .ix is deprecated from pandas verion- 0.19
    for i in range(n, len(df)):
        df['ATR'][i] = df['TR'][i-9:i+1].mean()

    # Calculation of SuperTrend
    df['Upper Basic'] = (df['high'] + df['low']) / 2 + (f * df['ATR'])
    df['Lower Basic'] = (df['high'] + df['low']) / 2 - (f * df['ATR'])
    df['Upper Band'] = df['Upper Basic']
    df['Lower Band'] = df['Lower Basic']
    for i in range(n, len(df)):
        if df['close'][i - 1] <= df['Upper Band'][i - 1]:
            df['Upper Band'][i] = min(df['Upper Basic'][i], df['Upper Band'][i - 1])
        else:
            df['Upper Band'][i] = df['Upper Basic'][i]
    for i in range(n, len(df)):
        if df['close'][i - 1] >= df['Lower Band'][i - 1]:
            df['Lower Band'][i] = max(df['Lower Basic'][i], df['Lower Band'][i - 1])
        else:
            df['Lower Band'][i] = df['Lower Basic'][i]
    df['SuperTrend'] = np.nan
    for i in range(n,len(df)):
        if df['close'][i] <= df['Upper Band'][i]:
            df['SuperTrend'][i] = df['Upper Band'][i]
        elif df['close'][i] > df['Upper Band'][i]:
            df['SuperTrend'][i] = df['Lower Band'][i]
    # for i in range(n, len(df)):
    #     if df['SuperTrend'][i - 1] == df['Upper Band'][i - 1] and df['close'][i] <= df['Upper Band'][i]:
    #         df['SuperTrend'][i] = df['Upper Band'][i]
    #     elif df['SuperTrend'][i - 1] == df['Upper Band'][i - 1] and df['close'][i] >= df['Upper Band'][i]:
    #         df['SuperTrend'][i] = df['Lower Band'][i]
    #     elif df['SuperTrend'][i - 1] == df['Lower Band'][i - 1] and df['close'][i] >= df['Lower Band'][i]:
    #         df['SuperTrend'][i] = df['Lower Band'][i]
    #     elif df['SuperTrend'][i - 1] == df['Lower Band'][i - 1] and df['close'][i] <= df['Lower Band'][i]:
    #         df['SuperTrend'][i] = df['Upper Band'][i]
    # df['signal']=np.nan
    # for i in range(n,len(df)):
    #     if df['SuperTrend'][i]>df['close'][i]:
    #         df['signal'][i]='BUY'
    #     else:
    #         df['signal'][i] = 'SELL'

    return df


con=sqlite3.connect('./sqldata/trade-database.db')
c=con.cursor()
c.execute('''DROP TABLE IF EXISTS super_trend''')


data=pd.read_sql_query("SELECT * FROM candle",con)
df=pd.DataFrame(data)

ST(df,3,10).to_sql('super_trend',con,if_exists='replace',index=True)
c.execute("SELECT * FROM super_trend")

pprint(c.fetchall())
con.commit()
con.close()




# from datetime import datetime
# from datetime import timedelta
#
# d=datetime.fromtimestamp(1566788)
# print(d)
# print(d+timedelta(seconds=60))
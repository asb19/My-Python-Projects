import pandas as pd
import sqlite3

conn = sqlite3.connect('./sqldata/trade-database.db')
c=conn.cursor()
# conn2=sqlite3.connect('./sqldata/candle.db')
def fifteenMinCandleGenerate():
    data=pd.read_sql_query("SELECT * FROM 1minCandle",conn,parse_dates=True)
    df=pd.DataFrame(data)
    # candle=df['LTP'].resample('1min').ohlc()
    # df['EXCHANGE_TIMESTAMP'] = pd.to_datetime(df['EXCHANGE_TIMESTAMP'], errors='coerce')
    df=df.set_index('EXCHANGE_TIMESTAMP')
    df.index=pd.DatetimeIndex(df.index)
    candle=df['LTP'].resample('15min').ohlc()
    c=conn.cursor()
    c.execute('''DROP TABLE IF EXISTS 1minCandle''')
    candle.to_sql('15mincandle',conn,if_exists='replace',index=True)
    c.execute("SELECT * FROM 15mincandle")
    print(c.fetchall())
    conn.commit()
    conn.close()
    return


fifteenMinCandleGenerate()






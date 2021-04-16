import csv
import datetime
import json
import sqlite3
import websocket
from datetime import datetime
import pandas as pd



access_token = "drYaso1oL8fGj74701Jw4NUP149pip92_4-hQKTYFx0.4dxp1T-JRErQd4R30Og0PSecsRYNtHst8VGy3FjJZfs"
conn = sqlite3.connect('./sqldata/trade-database.db')
c = conn.cursor()
resArray=[]
def oneMinCandleGenerate(resArray):


    df=pd.DataFrame(data=resArray,columns=["EXCHANGE_TIMESTAMP","LTP"])
    print(df)

    df=df.set_index('EXCHANGE_TIMESTAMP')
    df.index=pd.DatetimeIndex(df.index)
    candle=df['LTP'].resample('1min').ohlc()
    candle.to_sql('OneMinCandle',conn,if_exists='replace',index=True)
    conn.commit()
    return

def bytes_to_int(bytedata):
    result = 0

    for b in bytedata:
        result = result * 256 + int(b)
    return result
current_candle_time=0
open_time=0
def on_message(wb, message):
    print("received")
    res = list(message)
    # print(res)
    # global resArray
    global current_candle_time
    candleIs_same=True
    dt_obj = datetime.fromtimestamp(bytes_to_int(res[14:18]))
    print(dt_obj)
    seconds=dt_obj.second
    if current_candle_time!=0:
        if dt_obj.minute!=current_candle_time.minute:
            current_candle_time=dt_obj
            candleIs_same=False
    else:
        current_candle_time=dt_obj
    if candleIs_same==False:
        oneMinCandleGenerate(resArray)
    if bytes_to_int(res[6:10]) != 0:
        merest = [dt_obj, bytes_to_int(res[6:10]) / 100]
        resArray.append(merest)





    # if seconds==0:
    #     open_time=dt_obj
    #     print(open_time)
    # if open_time!=0 and dt_obj!=open_time+datetime.timedelta(seconds=59):
    #     print("data")
    #
    #     if bytes_to_int(res[6:10])!=0:
    #         merest = [dt_obj, bytes_to_int(res[6:10]) / 100]
    #         c.execute("INSERT INTO tick VALUES(?,?)", merest)
    #         c.execute("SELECT * FROM tick ORDER BY rowid DESC LIMIT 1;")
    #         print(c.fetchone())
    #         conn.commit()
    # else:
    #     oneMinCandleGenerate()



def on_open(wb):
    print('openned')
    data = {
        "a": "subscribe", "v": [[1, 1330]], "m": 'compact_marketdata'
    }
    wb.send(json.dumps(data))


socket = "wss://masterswift-beta.mastertrust.co.in/hydrasocket/v2/websocket?access_token=" + access_token
wb = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
wb.run_forever()

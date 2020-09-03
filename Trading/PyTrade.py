import csv
import datetime
import json
import sqlite3
import websocket

access_token = "9XqqozitJ3RVHIrUMVgIWZ1UB_tKsW_WAuLHwCWwVjY.8pJyTf5vyIV8ymYSTkPZuTXP873qGsvghxckC8SpsmY"
conn = sqlite3.connect('./sqldata/trade-database.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS trade (EXCHANGE_TIMESTAMP TEXT,LTP REAL)
""")


def bytes_to_int(bytedata):
    result = 0

    for b in bytedata:
        result = result * 256 + int(b)
    return result


def on_message(wb, message):
    print("received")
    res = list(message)
    # print(res)
    dt_obj = datetime.datetime.fromtimestamp(bytes_to_int(res[14:18]))
    seconds=dt_obj.second
    if bytes_to_int(res[6:10])!=0:
        merest = [dt_obj, bytes_to_int(res[6:10]) / 100]
        c.execute("INSERT INTO trade VALUES(?,?)", merest)
        c.execute("SELECT * FROM trade ORDER BY rowid DESC LIMIT 1;")
        print(c.fetchone())
        conn.commit()


def on_open(wb):
    print('openned')
    data = {
        "a": "subscribe", "v": [[1, 1330]], "m": 'compact_marketdata'
    }
    wb.send(json.dumps(data))


socket = "wss://masterswift-beta.mastertrust.co.in/hydrasocket/v2/websocket?access_token=" + access_token
wb = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
wb.run_forever()

import sqlite3
import pandas as pd

con=sqlite3.connect('./sqldata/trade-database.db')

data=pd.read_sql_query("SELECT * FROM candle",con)
print(data)



# from datetime import datetime
# from datetime import timedelta
#
# d=datetime.fromtimestamp(1566788)
# print(d)
# print(d+timedelta(seconds=60))
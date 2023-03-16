import csv
import psycopg2
import requests
import json


URL = "https://stg.saarthiapp.com/saarthi-data-service/user/verify?vertifyOpt=false"

headers = {
  'Content-Type': 'application/json'
}


conn = psycopg2.connect(
    host="34.93.202.34",
    database="postgres",
    user="postgres",
    password="selfCompassion",
    port="5432")

cur = conn.cursor()

print('PostgreSQL database version:')
cur.execute('SELECT phone FROM "User" limit 50;')




with open('usertoken.csv', 'w') as f:
    writer=csv.writer(f, delimiter='\t',lineterminator='\n',)
    for i in cur.fetchall():
        try:
            (phone,)=i
            print(phone)

            # this is api call kshitij
            r = requests.post(url=URL, verify=False, data=json.dumps({"phone": str(phone), "otp":"667","sessionId": "dnd"}),headers=headers )
            data=r.json() 
            #  this is json response
            print(data)
            token=[data['token']]
            print(token)
            writer.writerow(token)
            # here writing a
        except:
            print("error occured")

conn.close()


import requests
import json
import pandas as pd
import csv

headers = {
    'Content-Type': 'application/json',
}

params = (
    ('limit', '100'),
)

json_data = {
    'branch_key': 'key_live_dbRY4sqZDLp0rH6C7AUz1lfksueK2G5c',
    'branch_secret': 'secret_live_zoVaVkoS7q5XcSSFP4xC8Y1J6hefv583',
    'start_date': '2022-03-12',
    'end_date': '2022-03-12',
    'data_source': 'eo_click',
    'dimensions': [
        'last_attributed_touch_data_tilde_feature',
        'last_attributed_touch_data_tilde_channel',
        'last_attributed_touch_data_tilde_campaign',
        'last_attributed_touch_data_plus_current_feature',
    ],
    'filters': {
        '!last_attributed_touch_data_plus_current_feature': [
            'MOBILE_DEEPVIEWS',
            'DESKTOP_DEEPVIEWS',
        ],
    },
    'ordered': 'descending',
    'ordered_by': 'unique_count',
    'aggregation': 'unique_count',
    'zero_fill': True,
}

response = requests.post('https://api2.branch.io/v1/query/analytics', headers=headers, params=params, json=json_data).json()
print(response)

with open('usertoken.csv', 'w') as f:
    writer=csv.writer(f, delimiter='\t',lineterminator='\n',)
    data=response 
    print(data)
    results=data['results']
    for item in results:
        result = item['result']
        arrayToBeInserted = [result['unique_count'],result['last_attributed_touch_data_tilde_feature']]
        writer.writerow(arrayToBeInserted)
    
        
            

            # this is api call kshitij
            # r = requests.post(url=URL, verify=False, data=json.dumps({"phone": str(phone), "otp":"667","sessionId": "dnd"}),headers=headers )
        
            #  this is json response
        
        
            
            
            # here writing a new row
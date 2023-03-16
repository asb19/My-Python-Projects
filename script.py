import json


with open('s.txt') as f:
    data=f.read().splitlines()

# print('export INDIA_PROXY=\'%s\''%json.dumps(data))

with open('ss.txt', 'w') as f2:
    f2.write('export INDIA_PROXY=\'%s\''%json.dumps(data[200:300]))
import json
data={'name':'John','age':25}
with open('data.json','w') as f:
    json.dump(data,f)
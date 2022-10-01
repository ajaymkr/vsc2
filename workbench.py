import requests
import json

url_base = 'https://api.xdr.trendmicro.com'
url_path = '/v3.0/workbench/alerts'
token = 'YOUR_TOKEN'

query_params = {}
headers = {'Authorization': 'Bearer ' + token}

r = requests.get(url_base + url_path, params=query_params, headers=headers)

print(r.status_code)
if 'application/json' in r.headers.get('Content-Type', '') and len(r.content):
    print(json.dumps(r.json(), indent=4))
else:
    print(r.text)
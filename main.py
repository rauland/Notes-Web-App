import requests
import json
import cfg

url = "https://data.mongodb-api.com/app/data-yvjfn/endpoint/data/v1/action/findOne"

payload = json.dumps({
    "collection": "List",
    "database": "Reminders",
    "dataSource": "Cluster0",
    "projection": {
        "_id": 1
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': cfg.apikey, 
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

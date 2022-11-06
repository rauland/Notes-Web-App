import requests
import json
import cfg

def one(data):
    url = "https://data.mongodb-api.com/app/data-yvjfn/endpoint/data/v1/action/insertOne"

    payload = json.dumps({
        "collection": "List",
        "database": "Reminders",
        "dataSource": "Cluster0",
        "document": {
            "task": data
        }
    })

    headers = {
      'Content-Type': 'application/json',
      'Access-Control-Request-Headers': '*',
      'api-key': cfg.apikey, 
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response
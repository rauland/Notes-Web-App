import requests
import json
import cfg

def one():
    url = "https://data.mongodb-api.com/app/data-yvjfn/endpoint/data/v1/action/insertOne"

    payload = json.dumps({
        "collection": "List",
        "database": "Reminders",
        "dataSource": "Cluster0",
        "document": {
            "task":"Test data"
        }
    })

    headers = {
      'Content-Type': 'application/json',
      'Access-Control-Request-Headers': '*',
      'api-key': cfg.apikey, 
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

    return response
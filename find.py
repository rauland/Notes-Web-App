import requests
import json
import cfg

def all():
    url = "https://data.mongodb-api.com/app/data-yvjfn/endpoint/data/v1/action/find"

    payload = json.dumps({
        "collection": "List",
        "database": "Reminders",
        "dataSource": "Cluster0",
        "projection": {
            "task":1
        }
    })

    headers = {
      'Content-Type': 'application/json',
      'Access-Control-Request-Headers': '*',
      'api-key': cfg.apikey, 
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    response = json.loads(response.text)

    return response
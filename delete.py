import requests
import json
import cfg
from bson import ObjectId
from bson import json_util

def one(data):
    url = "https://data.mongodb-api.com/app/data-yvjfn/endpoint/data/v1/action/deleteOne"

    payload = json_util.dumps({
        "collection": "List",
        "database": "Reminders",
        "dataSource": "Cluster0",
        "filter": {
            "_id": ObjectId(data)
        }
    })
    print(payload)

    headers = {
      'Content-Type': 'application/json',
      'Access-Control-Request-Headers': '*',
      'api-key': cfg.apikey, 
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    response = json.loads(response.text)

    return response
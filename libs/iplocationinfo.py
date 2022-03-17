import requests
import json

def iploc(target):
    response = requests.get("http://ip-api.com/json/"+target)
    output=json.loads(response.text)
    
    return output
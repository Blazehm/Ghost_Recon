import requests
import json

def dnsresolveA(target): #Function to return Host Records
    response = requests.get("https://api.viewdns.info/dnsrecord/?domain="+target+"&recordtype=A&apikey=131f8092fc74a404acb826a4aa19877e86c1c766&output=json")
    output=json.loads(response.text)
    return output['response']['records']

def dnsresolveMX(target): #Function to return MX Records
    response = requests.get("https://api.viewdns.info/dnsrecord/?domain="+target+"&recordtype=MX&apikey=131f8092fc74a404acb826a4aa19877e86c1c766&output=json")
    output=json.loads(response.text)
    return output['response']['records']


import requests
import json
response = requests.get("https://api.viewdns.info/traceroute/?domain=twitter.com&apikey=131f8092fc74a404acb826a4aa19877e86c1c766&output=json")
output=json.loads(response.text)
print(output)
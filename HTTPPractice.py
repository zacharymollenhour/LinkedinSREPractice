import requests
import json

#Testing API/HTTP Calls with International Space Station
f_url = "http://api.open-notify.org/iss-now.json"
requestdata = requests.get(f_url)

#Parse Returned data
#print(requestdata.text)

#JSON Loads JSON DUMPS
#Converts string into a dictionary
tt = json.loads(requestdata.text)
print(tt)
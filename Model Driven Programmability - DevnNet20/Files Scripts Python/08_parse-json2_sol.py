#Replace 'your_api_key' with your MapQuest API key

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington"
dest = "Baltimore"
key = "your_api_key"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")


'''
DELETE
print(json_data)
'''

'''
OUTPUT:
URL: https://www.mapquestapi.com/directions/v2/route?key=your_api_key&to=Baltimore&from=Washington
API Status: 0 = A successful route call.

>>> 
'''

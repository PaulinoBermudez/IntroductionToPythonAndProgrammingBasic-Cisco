#Replace "your_api_key" with your MapQuest API key

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "your_api_key"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")

'''
OUTPUT
>>> 
 RESTART: /home/user/08_parse-json4_sol.py 
Starting Location: q
>>> 
 RESTART: /home/user/08_parse-json4_sol.py 
Starting Location: quit
>>> 
 RESTART: /home/user/08_parse-json4_sol.py 
Starting Location: Washington
Destination: q
>>> 
 RESTART: /home/user/08_parse-json4_sol.py 
Starting Location: Washington
Destination: quit
>>> 
'''

#!/bin/python
import os
os.system("clear")
os.system("cls")

import json
import requests

# Disable warning code
requests.packages.urllib3.disable_warnings()

# Create a variable named 'api_url' and assign the URL
api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback33"
# Create the dictionary variable named headers that has keys for Accept and Content-Type
# Assign the key and values.
headers = {
    "Accept":"application/yang-data+json",
    "Content-Type":"application/yang-data+json"
}

# Create variable authentication
basic_auth = ("cisco","cisco123!")

# Exec the delete request method.
resp = requests.delete(api_url, auth=basic_auth, headers=headers,verify=False)
response_json = resp.json()

print(json.dumps(response_json, indent=2))
#!/bin/python
import os
os.system("clear")
os.system("cls")

import json
import requests

# Deshabilitamos los warning existentes en el script
# Disable warning code
requests.packages.urllib3.disable_warnings()

# Create a variable named 'api_url' and assign the URL
api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces"
# Create the dictionary variable named headers that has keys for Accept and Content-Type
# Assign the key and values.
headers = {
    "Accept":"application/yang-data+json",
    "Content-Type":"application/yang-data+json"
}

# Create variable authentication
basic_auth = ("cisco","cisco123!")

# Send the get request method.
# Note: Disable verification of the SSL certificate
resp = requests.get(api_url, auth=basic_auth, headers=headers, verify=False)

# Evaluate the response
# Use the YANG model response values can be extracted from the response JSON.
response_json = resp.json()
# Verify the code return
print(response_json)

# Prettify the output, json.dumps() function with the indent parameters
read = input("\n Enter to continue ...")
os.system("clear")
os.system("cls")
print(json.dumps(response_json, indent=2))
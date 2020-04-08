#!/bin/python
import os
os.system("clear")
os.system("cls")

# Import the libraries
import json
import requests
import tabulate


from tabulate import *
from my_apic_em_functions import *

# Disable the warnings 
requests.packages.urllib3.disable_warnings()



# Built the request components
api_url = "https://sandboxapicem.cisco.com/api/v1/flow-analysis"
headers = {
    "content-type": "application/json"
}
body_json = {
    "username": "devnetuser",
    "password": "Cisco123!"
}

# Send the request
resp=requests.post(api_url,json.dumps(body_json),headers=headers,verify=False)

# Create the header dictionary
headers = []

i = 0
for item in response_json["response"]:
     i+=1
     host = [
             i,
             item["hostType"],
             item["hostIp"] 
            ]
     headers.append( host )
table_header = ["Number", "Type", "IP"]
print( tabulate(headers, table_header) )

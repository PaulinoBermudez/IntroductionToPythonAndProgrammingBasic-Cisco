#!/bin/python
# Import the libraries
import os
import json
import requests
import tabulate
from tabulate import *
from my_apic_em_functions import *
os.system("clear")
os.system("cls")

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


def devices_list:
    # Parse and format the JSON response data
    # Create a new list
    host_list = []

    # Generate the for loop to create a list
    i = 0
    for item in response_json["response"]:
        i+=1
        host = [
                i,
                item["hostType"],
                item["hostIp"] 
            ]
        host_list.append( host )
    table_header = ["Number", "Type", "IP"]
    print( tabulate(host_list, table_header) )


# Send the request
print("Show the TICKET NUMBER")
resp=requests.post(api_url,json.dumps(body_json),headers=headers,verify=False)

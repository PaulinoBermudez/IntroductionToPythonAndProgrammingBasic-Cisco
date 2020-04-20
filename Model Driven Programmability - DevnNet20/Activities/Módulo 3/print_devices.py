#!/bin/python
import os
os.system("clear")
os.system("cls")

import requests
import json
import tabulate


from tabulate import *
from my_apic_em_functions import *

# Built the request components
api_url = "https://sandboxapicem.cisco.com/api/v1/network-device"
ticket = get_ticket()
headers = {
 "content-type": "application/json",
 "X-Auth-Token": ticket
}
# Request and handle errors.
resp = requests.get(api_url, headers=headers, verify=False)
os.system("clear")
os.system("cls")

print("Status of /host request: ", resp.status_code)
if resp.status_code != 200:
    raise Exception("Status code does not equal 200. Response text: " + resp.text)
response_json = resp.json()


# Parse and format the JSON response data
# Create a new list
devices_list = []

# Generate the for loop to create a list
i = 0
for item in response_json["response"]:
    i+=1
    host = [
             i,
             item["location"],
             item["type"],
             item["managementIpAddress"], 
             item["serialNumber"],
             item["family"],
             item["hostname"]
            ]
    devices_list.append( host )
table_header = ["Number", "Location","Type", "IP", "S/N", "Family", "hostname"]
print( tabulate(devices_list, table_header) )


# print("Print the all information devices")
# print("---------------------------------------------------")
# print(response_json)
# print("---------------------------------------------------")
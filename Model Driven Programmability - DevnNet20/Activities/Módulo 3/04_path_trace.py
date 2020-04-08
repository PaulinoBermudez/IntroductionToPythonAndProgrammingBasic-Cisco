#!/bin/python
# Import the libraries
import os
import json
import requests
import tabulate
os.system("clear")
os.system("cls")

from tabulate import *
print("--------------------------")
print ("TICKET STATUS CODE ")
print("--------------------------")
from my_apic_em_functions import *

print("--------------------------")
print("LIST OF HOST ON THE NET")
print("--------------------------")
from print_host import *

print("--------------------------")
print("LIST OF DEVICES ON THE NET")
print("--------------------------")
from print_devices import *

print('List of hosts on the network: ')
print (tabulate(host_list,headers=['Number','Type','IP'],tablefmt='rst'))
print('\n') #prints blank line to format output
print('List of devices on the network: ')
print (tabulate(devices_list,headers=['Number','Type','IP'],tablefmt='rst'))



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
resp=requests.post(api_url,json.dumps(body_json),headers=headers,verify=False)

# SECTION 3. Get the source and destination IP Add for the Path Trace

while True:
    # Source
    s_ip = input("Please, Write the SOURCE IP address for the path trace: ") 
    # Destination
    d_ip = input("Please, Write the DESTINATION IP address for the path trace: ")
    # Error messages
    if s_ip != '' or d_ip != '':
        # Create the Python library
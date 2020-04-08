#!/bin/python
# Import the libraries
import os
import json
import requests
import tabulate
import threading
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

# S.4 - SECTION 3. Get the source and destination IP Add for the Path Trace

while True:
    # In this test, I'm using all the time the same IP Address and save time
    # Source
    s_ip = '165.10.1.39'
    # Destination
    d_ip = '10.1.15.117'
    # Error messages
    if s_ip != '':
        print("Source ... OK!")
        if d_ip != '':
            # Create the Python dictionary 
            path_data = {
                "sourceIP": s_ip,
                "destIP":d_ip
            }
            print("Destination IP  ... OK!")
        else:
            print("Destination IP ... Fail")
            print(" YOU MUST ENTER IP ADDRESS TO CONTINUE ... ")
            print(" Push CTRL+C to quit program")
            continue
        print("---------- YOUR DATA -------------")
        print("Source IP address: " + path_data['sourceIP'])
        print("Destination IP address: " + path_data['destIP'])
        break
    else:
        print(" YOU MUST ENTER IP ADDRESS TO CONTINUE ... ")
        print(" Push CTRL+C to quit program")
        continue

# S.4-5 - Complete the code for section 4 to initiate the path trace and get the flow analysis ID.

# Variable to hold the path_data
path = json.dumps(path_data)
resp = requests.post(api_url,path, headers=headers, verify=False)

# # Inspect the return, get the Flow  Analysis ID
resp_json=resp.json()
flowAnalysisId=resp_json["response"]["flowAnalysisId "]
print("Flow Analysis ID:" + flowAnalysisId )
print(path)

#============================
# Section 4. Initiate the Path Trace and get the flowAnalysisId
#============================

#++++++++++++++++++++++++++++++++++++		
# Post request to initiate Path Trace
path = json.dumps(path_data) #variable to hold the path_data
resp = requests.post(api_url,path,headers=headers,verify=False)

# Inspect the return, get the Flow Analysis ID, put it into a variable
response_json = resp.json()

try:
    flowAnalysisId = response_json['response']['flowAnalysisId']
    print('FLOW ANALYSIS ID: ' + flowAnalysisId)
    print(path)
except:
    print ("\n For some reason cannot get flowAnalysisId")
print(api_url)
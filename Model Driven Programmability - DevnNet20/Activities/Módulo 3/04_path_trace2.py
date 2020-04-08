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
from my_apic_em_functions import *
from print_devices import *
from print_host import *

print("--------------------------")
from my_apic_em_functions import *


###################################
#               HOST              #
###################################


# Create the 'get_ticket' function
def get_ticket():
    api_url = "https://sandboxapicem.cisco.com/api/v1/ticket"
    headers = {
        "content-type": "application/json"
    }
    body_json = {
        "username": "devnetuser",
        "password": "Cisco123!"
    }
    # Send the request
    resp=requests.post(api_url,json.dumps(body_json),headers=headers,verify=False)
    #  Print the response and see the status 
    print("______________________________________________________")
    print("Ticket request status: ", resp.status_code)
    response_json = resp.json()
    serviceTicket = response_json["response"]["serviceTicket"] 
    print("The service ticket number is: ", serviceTicket)
    print("______________________________________________________")
    return serviceTicket

# Built the request components
api_url = "https://sandboxapicem.cisco.com/api/v1/host"
ticket = get_ticket()
headers = {
 "content-type": "application/json",
 "X-Auth-Token": ticket
}
# Request and handle errors.
resp = requests.get(api_url, headers=headers, verify=False)
print("Status of /host request: ", resp.status_code)
if resp.status_code != 200:
    raise Exception("Status code does not equal 200. Response text: " + resp.text)
response_json = resp.json()


# Parse and format the JSON response data
# Create a new list
host_list = []

# Generate the for loop to create a list
i = 0
for item in response_json["response"]:
     i+=1
     host = [
             i,
             item['hostType'],
             item['hostIp'] 
            ]
     host_list.append( host )
table_header = ["Number", "Type", "IP"]
print( tabulate(host_list, table_header) )

###################################
#             DEVICES             #
###################################

# Built the request components
api_url = "https://sandboxapicem.cisco.com/api/v1/network-device"
ticket = get_ticket()
headers = {
 "content-type": "application/json",
 "X-Auth-Token": ticket
}
# Request and handle errors.
resp = requests.get(api_url, headers=headers, verify=False)

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

print("--------------------------")

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
    s_ip = "10.2.1.22"
    # Destination
    d_ip = "10.1.15.117"
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

#============================
# Section 4. Initiate the Path Trace and get the flowAnalysisId
#============================

#++++++++++++++++++++++++++++++++++++		
# Post request to initiate Path Trace
print("....................................................................")
print("The URL is: " + api_url)
print("....................................................................")
#variable to hold the path_data
path = json.dumps(path_data) 
resp = requests.post(api_url,path,headers=headers,verify=False)

# Inspect the return, get the Flow Analysis ID, put it into a variable
response_json = resp.json()
print(response_json)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# I have a extract to API > Flow Analysis > POST > flowAnalysisRequest	>
#   {"destIP": "10.2.1.22", "inclusions": ["INTERFACE-STATS", "DEVICE-STATS"], "sourceIP": "10.1.15.117", "periodicRefresh": false}
# Value: 
flowAnalysisId="ce33b3e1-707d-498e-97bb-bc3b264a13dd"
try:
    flowAnalysisId=response_json["response"]["flowAnalysisId"]
    print("FLOW ANALYSIS ID: " + flowAnalysisId)
    print(path)
except:
    print ("\n For some reason cannot get flowAnalysisId")

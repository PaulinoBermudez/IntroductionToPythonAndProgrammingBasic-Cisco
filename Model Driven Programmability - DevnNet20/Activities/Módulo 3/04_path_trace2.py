#!/bin/python
# Import the libraries
import os
import json
import request
import requests
import tabulate
import sys
import threading
os.system("clear")
os.system("cls")

from tabulate import *
#from my_apic_em_functions import *
#from print_devices import *
#from print_host import *

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
# print( tabulate(host_list, table_header) )

print("============================ HOST =========================================================")
NADA=input("Pulse para continuar") 
os.system("clear")
os.system("cls")
print("=====================================================================================================")
 





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
# print( tabulate(devices_list, table_header) )
# print('List of hosts on the network: ')
# print('\n') #prints blank line to format output
# print('List of devices on the network: ')

print("OK! [>              ] ")
print("OK! [===>           ] ")
print("OK! [======>        ] ")
print("OK! [===========>   ] ")
print("OK! [==============>] ")

print("")
print("============================ DEVICES =========================================================")
NADA=input("Pulse para continuar") 
os.system("clear")
os.system("cls")
print("=====================================================================================================")
 

print (tabulate(host_list,headers=['Number','Type','IP','MODEL','TYPE2','LOCATION'],tablefmt='rst'))
print (tabulate(devices_list,headers=['Number','Type','IP','MODEL','TYPE2','LOCATION'],tablefmt='rst'))


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


print("....................................................................")
print("The URL is: " + api_url)
print("The PATH is: " + json.dumps(path_data))
print("....................................................................")
NADA=input("Pulse para continuar .... ")
resp = requests.post(api_url,json.dumps(path_data),headers=headers,verify=False)

#++++++++++++++++++++++++++++++++++++++	
# Post request to initiate Path Trace +
#variable to hold the path_data       +
path=json.dumps(path_data)
# Inspect the return, get the Flow Analysis ID, put it into a variable
resp_json = resp.json()

print(resp)
print(resp_json)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
try:
    flowAnalysisId=response_json["response"]["flowAnalysisId"]
    print("FLOW ANALYSIS ID: " + flowAnalysisId)
    print(path)
except:
    print ("\n For some reason cannot get flowAnalysisId")
# I have a extract to API > Flow Analysis > POST > flowAnalysisRequest	>
#   {"destIP": "10.2.1.22", "inclusions": ["INTERFACE-STATS", "DEVICE-STATS"], "sourceIP": "10.1.15.117", "periodicRefresh": false}
# Value: 
flowAnalysisId="ce33b3e1-707d-498e-97bb-bc3b264a13dd"
print('FLOW ANALYSIS ID: ' + flowAnalysisId)
print(path)


#=========================================================================================================
# Section 5-6 Check status of Path Trace request, output results when COMPLETED
#=========================================================================================================
print("This section might take some time to run")
status = ""

#Add Flow Analysis ID to the endpoint URL in order to check the status of this specific path trace
check_url = api_url + "/" + flowAnalysisId
# Variable to increment within the while loop. Will trigger exit from loop after x iterations
checks = 0 
print ("START - Current date and time: ")
while status != 'COMPLETED':
    checks += 1
    r = requests.get(check_url,headers=headers,params="",verify = False)
    response_json = r.json()
    status = response_json["response"]["request"]["status"]
    print('REQUEST STATUS: ' + status)
    #number of iterations before exit of loop; change depending on conditions
    if checks == 15:
        print("Number of status checks exceeds limit. Possible problem with Path Trace.")
        break
    elif status == 'FAILED':
        print('Problem with Path Trace')
        print('Problem with FlowAnalysisId: ' + check_url)
        break
    print('REQUEST STATUS: ' + status)
print(check_url)
print("Response in json format")
print ('==============================================================')
print(response_json)
print ('==============================================================')


#============================
# Section 6-7. Display results
#============================

#+++++++++++Add Values+++++++++++++++
# Create required variables
path_source = response_json['response']['request']['sourceIP'] 	#the source address for the trace, printed below
path_dest = response_json['response']['request']['destIP'] 	#the destination address for the trace, printed below
networkElementsInfo = response_json['response']['networkElementsInfo'] 	#variable holding a list of all the network element dictionaries


print("Responses are being processed")
print("Path Source "+path_source)
print("Path Dest "+path_dest)
print("Network Elements Information "+json.dumps(networkElementsInfo))

all_devices = [] # create a list variable to store the hosts and devices
device_no = 1  #this variable is an ordinal number for each device, incremented in the loop

#Iterate through returned Path Trace JSON and populate list of path information
for networkElement in networkElementsInfo:
    # test if the devices DOES NOT have a "name", absence of "name" identifies an end host
    if not 'name' in networkElement:  #assigns values to the variables for the hosts
       name = 'Unnamed Host'
       ip = networkElement['ip']
       egressInterfaceName = 'UNKNOWN'
       ingressInterfaceName = 'UNKNOWN'
       device = [device_no,name,ip,ingressInterfaceName,egressInterfaceName]
    # if there is the "name" key, then it is an intermediary device
    else: #assigns values to the variables for the intermediary devices
       name = networkElement['name']
       ip = networkElement['ip']   
       if 'egressInterface' in networkElement: #not all intermediary devices have ingress and egress interfaces
           egressInterfaceName = networkElement['egressInterface']['physicalInterface']['name']
       else:
           egressInterfaceName = 'UNKNOWN'
           
       if 'ingressInterface' in networkElement:
           ingressInterfaceName = networkElement['ingressInterface']['physicalInterface']['name']
       else:
           ingressInterfaceName = 'UNKNOWN'       
       device = [device_no,name,ip,ingressInterfaceName,egressInterfaceName] #create the list of info to be displayed
    all_devices.append(device) #add this list of info for the device as a new line in this variable
    device_no += 1  #increments the ordinal variable for the device in the list

print("Looping through all the devices")

# Step 8. Exec and see the result
print('Path trace \n Source: ' + path_source + '\n Destination: ' + path_dest) #print the source and destination IPs for the trace
print('List of devices on path:')
print (tabulate(all_devices,headers=['Item','Name','IP','Ingress Int','Egress Int'],tablefmt="rst")) #print the table of devices in the path trace


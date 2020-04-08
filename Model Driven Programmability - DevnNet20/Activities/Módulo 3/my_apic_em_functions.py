#!/bin/python
import os
#os.system("clear")
#os.system("cls")

import requests
import json
import tabulate


from tabulate import *
# from my_apic_em_functions import *

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


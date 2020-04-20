#!/bin/python
import os
os.system("clear")
os.system("cls")

# Import the libraries
import json
import requests
# Disable the warnings 
requests.packages.urllib3.disable_warnings()
# Built the request components
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
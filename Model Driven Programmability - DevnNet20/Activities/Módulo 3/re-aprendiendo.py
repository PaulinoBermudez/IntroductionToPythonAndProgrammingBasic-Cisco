#!/bin/python 
import os
os.system('clear')
os.system('cls')
# @author: [ Paulino Bermúdez R.]
# @Description: se me fue la pinsa y tengo que volver a aprender a crear las peticiones a la API.

import requests
import json

# Disable warnings SSL
requests.packages.urllib3.disable_warnings()

# Variables
apic_em_ip = "https://sandboxapicem.cisco.com/api/v1"
api_call ="/ticket"

# Combine these variables into one variable
url = apic_em_ip + api_call

# Payload with authentication information
payload = {"username":"devnetuser","password":"Cisco123!"}

# Headers
headers = {"content-type" : "application/json"}

# Assign the response to a variable
response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False).json()

# Print the Token
print("Authenticaton Token: " , response["response"]["serviceTicket"])
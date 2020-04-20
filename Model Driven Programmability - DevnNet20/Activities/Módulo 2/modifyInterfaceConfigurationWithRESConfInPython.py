#!/bin/python
import os
os.system("clear")
os.system("cls")

import json
import requests

# Disable warning code
requests.packages.urllib3.disable_warnings()

# Create a variable named 'api_url' and assign the URL
api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback33"
# Create the dictionary variable named headers that has keys for Accept and Content-Type
# Assign the key and values.
headers = {
    "Accept":"application/yang-data+json",
    "Content-Type":"application/yang-data+json"
}

# Create variable authentication
basic_auth = ("cisco","cisco123!")

# Create a Python dictionary variable yangConfig holding the YANG data to create new interface 'Looback33'.

yangConfig = {
    "ietf-interfaces:interface":{
        "name":"Loopback33",
        "description":"Interface Testing Created with Python Code",
        "type":"iana-if-type:softwareLoopback",
        "enabled":True,
        "ietf-ip:ipv4":{
            "address":[
                {
                    "ip":"33.33.33.33",
                    "netmask":"255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6":{}
    }
}

# Send the Put request. 

resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basic_auth, headers= headers, verify=False )
if (resp.status_code >= 200 and resp.status_code <= 299 ):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print("ERROR CODE {}, reply: {}".format(resp.status_code, resp.json()))
print("If you don't recongnize the status code, see: https://http.cat/")
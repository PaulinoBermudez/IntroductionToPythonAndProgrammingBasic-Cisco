#!/bin/python
import os
os.system("clear")
os.system("cls")

sshCli = ConnectHandler(
    device_type='cisco_ios',
    host='192..168.156.101',
    port=22,
    username='cisco',
    password='cisco123!'
)

URL='https://192.168.56.101/'
directory='restconf/data/'

api_url = "URL/directory/ietf-interfaces:interfaces"
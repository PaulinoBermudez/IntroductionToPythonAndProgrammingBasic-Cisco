#!/bin/python
import os
os.system("clear")
os.system("cls")

# Install the library in the SO
# apt-get install -y python-netmiko || pip install netmiko


# Import the netmiko library
import netmiko

# Import 'connecthandler()' function from the netmiko module.
from netmiko import ConnectHandler()

# Setup SSHClient connection object using the ConnectHandler() function to the IOS XE device.
sshCli = ConnectHandler(
     device_type='cisco_ios',
    host='192..168.156.101',
    port=22,
    username='cisco',
    password='cisco123!'
)

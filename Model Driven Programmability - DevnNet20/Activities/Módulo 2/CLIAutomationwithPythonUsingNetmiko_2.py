#!/bin/python
import os
os.system("clear")
os.system("cls")

# Install the library in the SO
# apt-get install -y python-netmiko || pip install netmiko

# Import the netmiko library
import netmiko

# Import 'connecthandler()' function from the netmiko module.
from netmiko import ConnectHandler

# Setup SSHClient connection object using the ConnectHandler() function to the IOS XE device.
''' INFORMATION VARIABLES.
    -  Device_type: Identifies the remote device type.
    -  Host: The address (host or IP) of the remote device (adjust the IP address "192.168.56.X") to match your router's current address.
    -  Port: The remote port of the SSH Service
    -  Username: Remote SSH Username (in this lab "cisco" for that was setup in the IOS XE VM)
    -  Password: Remote SSH password (in this lab "cisco123!" for that was setup in the IOS XE VM)
'''
sshCli = ConnectHandler(
    device_type='cisco_ios',
    host='192.168.56.101',
    port=22,
    username='cisco',
    password='cisco123!'
)
# Comand code who send the router Cisco, configure the new Interface device - Loopback 1.
config_commands = [
    'int loopback 190',
    'ip address 190.190.190.190 255.255.255.0',
    'description LAB INTERFACE'
]
# Output configuration commands.
output1 = sshCli.send_config_set(config_commands)
# Sent some simple commands and display the returned output
print("Sendind 'sh ip int brief' ... ")
output2 = sshCli.send_command("show ip int brief")
print("show ip int brief: \n{}\n".format(output2))
print("_________________________________________")
print("Config output from the device: \n{}\n".format(output1))

config_commands = [
    'int loopback 2',
    'ip address 2.2.2.2 255.255.255.0',
    'description LAB INTERFACE2'
]
# Output configuration commands.
output3 = sshCli.send_config_set(config_commands)
# Sent some simple commands and display the returned output
print("Sendind 'sh ip int brief' ... ")
print("_________________________________________")
print("Config output from the device: \n{}\n".format(output3))
print("_________________________________________")
print("Print all info: \n")
print("Show the IP brief: \n{}\n".format(output2))

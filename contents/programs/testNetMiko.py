#!/usr/bin/env python3

from netmiko import ConnectHandler

sshovercli = ConnectHandler(device_type='cisco_ios', host='192.168.56.101',port="22", username="cisco", password="cisco123!")

# output = sshovercli.send_command("show ip interface brief")
output = sshovercli.send_command("sh ip int brief")

configCommands =  ['int loopback', 'ip address 1.2.3.4 255.255.255.0', 'description loopback over ssh']
outputConfig = sshovercli.send_config:_set(ConfigCommands)
output1 = device.send_command("show running-config")
print(output1)
print("\n")
print ("Show ip interface brief: \n {}".format(output))



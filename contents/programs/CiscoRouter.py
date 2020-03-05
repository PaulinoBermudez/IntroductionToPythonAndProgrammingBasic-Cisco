#!/bin/usr/env python

from netmiko import ConnectHandler

iou1 = {
    'device_type':'cisco_ios',
    'ip': '192.168.56.100',
    'username':'cisco'
    'password':'cisco123!'
}

device = ConnectHandler(**iou1)

output1 = device.send_command("show running-config")
seve_file = open("Switch_running.txt","w")
seve_file.write(output1)
save_file.close()
device.disconnect()
#!/bin/python
import os
os.system("clear")
os.system("cls")

from ncclient import manager
manager = manager.connect(
    host="192.168.56.101",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)
netconf_reply  = manager.get_config(source="running")
print(netconf_reply)
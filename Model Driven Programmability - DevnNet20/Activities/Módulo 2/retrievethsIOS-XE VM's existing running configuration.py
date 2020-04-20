#!/bin/python
import os
os.system("clear")
os.system("cls")

from ncclient import manager

with manager.connect(
    host="192.168.56.101",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)as m:
    c = m.get_config(source='running').data_xml
    with open("%s.xml" % host, 'w') as f:
        f.write(c)
        
netconf_reply  = manager.get_config(source="running")
print(netconf_reply) 
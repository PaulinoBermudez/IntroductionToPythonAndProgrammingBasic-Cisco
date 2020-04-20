#!/bin/python
import os
os.system("clear")
os.system("cls")

from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    host="192.168.56.101",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)
        
netconf_reply  = manager.get_config(source="running")
print(netconf_reply) 

netconf_data = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>NEWHOSTNAME</hostname>
    </native>
</config>
"""
# Edit the existing device configuration with the "edit_config()" function of the "m" NETConf session object. The edit_config() function 
# expects two parameters:
#   - target: The target netconf data-store to be updated.
#   - config: the configuration update.
#
# The edit_config() function returns and XML object containing information about the change success. After editing the configuration, print the 
# returned value:
netconf_reply = m.edit_config(target="running", config=netconf_data)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
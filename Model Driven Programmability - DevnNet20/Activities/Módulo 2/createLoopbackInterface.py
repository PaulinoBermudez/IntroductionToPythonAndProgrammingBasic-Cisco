#!/bin/python
import os
import ncclient
import xml.dom.minidom

os.system("clear")
os.system("cls")

from ncclient import manager


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
        <interface>
            <Loopback>
                <name>100</name>
                <description>TEST1</description>
                <ip>
                    <address>
                        <primary>
                            <address>100.100.100.100</address>
                            <mask>255.255.255.0</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_data)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
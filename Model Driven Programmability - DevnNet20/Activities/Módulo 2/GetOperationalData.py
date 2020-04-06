#!/bin/python
import os
import ncclient
import xml.dom.minidom
import xmltodict
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

netconf_filter = """
<filter>
    <interfaces-state xmlns = "urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
</filter>
"""

netconf_reply = m.get(filter = netconf_filter)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# Converting the XML netconf_reply data to a Python dictionary using the “xmltodict” module
netconf_reply_dict = xmltodict.parse(netconf_reply.xml)
for interface in netconf_reply_dict["rpc-reply"]["data"]["interface-state"]["interface"]:
    print("Name: {} MAC: {} Input: {} Output: {}".format(
            interface["name"],
            interface["phys-address"],
            interface["statistics"]["in-octets"],
            interface["statistcs"]["out-octets"]
        )
    )
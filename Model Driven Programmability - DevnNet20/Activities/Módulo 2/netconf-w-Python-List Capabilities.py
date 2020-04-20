#!/bin/python
import os
os.system("clear")
os.system("cls")

# install the ncclient Python module
# pip install ncclient

import ncclient
from ncclient import manager

manager = manager.connect(
    host="192.168.56.101",
    # Remote port of the NETConf service
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)

print("#Supported Capabilities (YANG models):")
for capability in manager.server_capabilities:
    print(capability)
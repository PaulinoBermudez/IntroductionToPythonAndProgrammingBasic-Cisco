#!/bin/python

import os
os.system("clear")
os.system("cls")
# Data inputs
nativeVLAN = 101
dataVLAN = 100
# Conditionals
if nativeVLAN == dataVLAN:
    print("The native VLAN and the data VLAN are the same.")
else:
    print("The native VLAN and the data VLAN is different.")